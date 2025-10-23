import json
import os
from src.models.tarefa import Tarefa

class TarefaService:
    def __init__(self, arquivo="tarefas.json"):
        self._arquivo = arquivo
        if not os.path.exists(self._arquivo):
            with open(self._arquivo, "w") as f:
                json.dump([], f)

    def _carregar_tarefas(self):
        if not os.path.exists(self._arquivo):
            return []

        with open(self._arquivo, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [Tarefa(**t) for t in data]

    def _salvar_tarefas(self, tarefas):
        with open(self._arquivo, "w") as f:
            json.dump([t.to_dict() for t in tarefas], f, indent=4)

    # MÉTODO CRIAR TAREFA
    def criar_tarefa(self, titulo, descricao):
        tarefas = self._carregar_tarefas()
        nova_tarefa = Tarefa(id=len(tarefas) + 1, titulo=titulo, descricao=descricao)
        tarefas.append(nova_tarefa)
        self._salvar_tarefas(tarefas)
        return nova_tarefa


    # LISTAR TODAS AS TAREFAS
    def listar_tarefas(self):
        return self._carregar_tarefas()

    # ATUALIZAR STATUS
    def atualizar_status(self, id_tarefa, novo_status):
        tarefas = self._carregar_tarefas()
        for tarefa in tarefas:
            if tarefa.id == id_tarefa:
                tarefa.status = novo_status
                self._salvar_tarefas(tarefas)
                return tarefa
        return None

    # EXCLUIR TAREFA
    def excluir_tarefa(self, id_tarefa):
        tarefas = self._carregar_tarefas()
        tarefas = [t for t in tarefas if t.id != id_tarefa]
        self._salvar_tarefas(tarefas)



