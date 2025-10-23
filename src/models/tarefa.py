from enum import Enum
from datetime import datetime

class Status(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"

class Tarefa:
    def __init__(self, id, titulo, descricao, status="Pendente", data_criacao=None, **kwargs):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status if isinstance(status, Status) else Status(status)
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_criacao": self.data_criacao,
            "status": self.status.value
        }

    @staticmethod
    def from_dict(data):
        status = Status(data["status"])
        tarefa = Tarefa(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data["descricao"],
            status=status
        )
        tarefa.data_criacao = data["data_criacao"]
        return tarefa

