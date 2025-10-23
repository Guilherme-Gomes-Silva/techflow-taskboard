import json
import os
from src.models.tarefa import Tarefa


class TarefaService:
    """
    Serviço responsável pelo gerenciamento de tarefas.

    Este serviço permite criar, listar, atualizar o status e excluir tarefas,
    armazenando os dados em um arquivo JSON.
    """

    def __init__(self, arquivo="tarefas.json"):
        """
        Inicializa o serviço, garantindo que o arquivo de armazenamento exista.

        Args:
            arquivo (str): Caminho do arquivo JSON onde as tarefas serão salvas.
        """
        self._arquivo = arquivo
        if not os.path.exists(self._arquivo):
            with open(self._arquivo, "w") as f:
                json.dump([], f)

    def _carregar_tarefas(self):
        """
        Carrega as tarefas do arquivo JSON.

        Returns:
            list[Tarefa]: Lista de objetos Tarefa carregados do arquivo.
        """
        if not os.path.exists(self._arquivo):
            return []

        with open(self._arquivo, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # Retorna lista vazia caso o arquivo esteja corrompido
                return []

        return [Tarefa(**t) for t in data]

    def _salvar_tarefas(self, tarefas):
        """
        Salva a lista de tarefas no arquivo JSON.

        Args:
            tarefas (list[Tarefa]): Lista de objetos Tarefa a serem salvos.
        """
        with open(self._arquivo, "w") as f:
            json.dump([t.to_dict() for t in tarefas], f, indent=4)

    # MÉTODO CRIAR TAREFA
    def criar_tarefa(self, titulo, descricao):
        """
        Cria uma nova tarefa e a adiciona ao arquivo.

        Args:
            titulo (str): Título da nova tarefa.
            descricao (str): Descrição detalhada da tarefa.

        Returns:
            Tarefa: A instância da tarefa criada.
        """
        tarefas = self._carregar_tarefas()
        nova_tarefa = Tarefa(id=len(tarefas) + 1, titulo=titulo, descricao=descricao)
        tarefas.append(nova_tarefa)
        self._salvar_tarefas(tarefas)
        return nova_tarefa

    # LISTAR TODAS AS TAREFAS
    def listar_tarefas(self):
        """
        Retorna todas as tarefas cadastradas.

        Returns:
            list[Tarefa]: Lista de todas as tarefas.
        """
        return self._carregar_tarefas()

    # ATUALIZAR STATUS
    def atualizar_status(self, id_tarefa, novo_status):
        """
        Atualiza o status de uma tarefa específica.

        Args:
            id_tarefa (int): ID da tarefa a ser atualizada.
            novo_status (Status): Novo status da tarefa.

        Returns:
            Tarefa | None: Tarefa atualizada ou None se não encontrada.
        """
        tarefas = self._carregar_tarefas()
        for tarefa in tarefas:
            if tarefa.id == id_tarefa:
                tarefa.status = novo_status
                self._salvar_tarefas(tarefas)
                return tarefa
        return None

    # EXCLUIR TAREFA
    def excluir_tarefa(self, id_tarefa):
        """
        Remove uma tarefa com base no ID.

        Args:
            id_tarefa (int): ID da tarefa a ser excluída.
        """
        tarefas = self._carregar_tarefas()
        tarefas = [t for t in tarefas if t.id != id_tarefa]
        self._salvar_tarefas(tarefas)
