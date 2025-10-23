from enum import Enum
from datetime import datetime


class Status(Enum):
    """
    Enum que representa o status de uma tarefa.

    Cada valor corresponde a uma fase do ciclo de vida da tarefa:
    - PENDENTE: tarefa criada, mas ainda não iniciada.
    - EM_ANDAMENTO: tarefa atualmente em execução.
    - CONCLUIDA: tarefa finalizada com sucesso.
    """

    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"

    @staticmethod
    def from_string(texto):
        """
        Converte uma string em um valor do Enum `Status`.
        Args:
            texto (str): O texto representando o status (ex: "pendente", "em andamento").
        Returns:
            Status: O valor correspondente do Enum.
        Raises:
            ValueError: Caso o texto não corresponda a nenhum status válido.
        """
        texto = texto.strip().lower()
        if texto == "pendente":
            return Status.PENDENTE
        elif texto in ("em andamento", "em_andamento"):
            return Status.EM_ANDAMENTO
        elif texto == "concluída":
            return Status.CONCLUIDA
        else:
            raise ValueError(f"Status inválido: {texto}")


class Tarefa:
    """
    Classe que representa uma tarefa no sistema de gerenciamento.

    Cada tarefa possui um ID único, título, descrição, status e data de criação.
    """

    def __init__(self, id, titulo, descricao, status="Pendente", data_criacao=None, **kwargs):
        """
        Inicializa uma nova instância da classe Tarefa.

        Args:
            id (int): Identificador único da tarefa.
            titulo (str): Título descritivo da tarefa.
            descricao (str): Texto explicando o que deve ser feito.
            status (str | Status): Estado atual da tarefa.
            data_criacao (str, opcional): Data e hora de criação.
        """
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status if isinstance(status, Status) else Status(status)
        self.data_criacao = data_criacao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """
        Converte o objeto Tarefa em um dicionário.

        Returns:
            dict: Representação serializável da tarefa.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_criacao": self.data_criacao,
            "status": self.status.value
        }

    @staticmethod
    def from_dict(data):
        """
        Cria uma instância de Tarefa a partir de um dicionário.

        Args:
            data (dict): Dicionário contendo os dados da tarefa.
        Returns:
            Tarefa: Objeto Tarefa reconstruído a partir do dicionário.
        """
        status = Status(data["status"])
        tarefa = Tarefa(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data["descricao"],
            status=status
        )
        tarefa.data_criacao = data["data_criacao"]
        return tarefa
