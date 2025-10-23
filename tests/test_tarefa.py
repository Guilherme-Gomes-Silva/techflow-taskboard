import pytest
from src.models.tarefa import Tarefa, Status
from src.services.tarefa_service import TarefaService

@pytest.fixture
def service(tmp_path):
    """Cria uma instância do serviço usando um arquivo temporário"""
    arquivo = tmp_path / "tarefas.json"
    return TarefaService(arquivo=str(arquivo))

def test_criar_tarefa(service):
    t = service.criar_tarefa("Comprar leite", "Ir ao mercado")
    assert t.id == 1
    assert t.titulo == "Comprar leite"
    assert t.descricao == "Ir ao mercado"
    assert t.status == Status.PENDENTE

def test_listar_tarefas(service):
    service.criar_tarefa("Comprar leite", "Ir ao mercado")
    service.criar_tarefa("Estudar Python", "Praticar pytest")
    tarefas = service.listar_tarefas()
    assert len(tarefas) == 2
    assert tarefas[0].titulo == "Comprar leite"
    assert tarefas[1].titulo == "Estudar Python"

def test_atualizar_status(service):
    t = service.criar_tarefa("Comprar leite", "Ir ao mercado")
    t_atualizada = service.atualizar_status(t.id, Status.CONCLUIDA)
    assert t_atualizada.status == Status.CONCLUIDA

def test_excluir_tarefa(service):
    t1 = service.criar_tarefa("Comprar leite", "Ir ao mercado")
    t2 = service.criar_tarefa("Estudar Python", "Praticar pytest")
    service.excluir_tarefa(t1.id)
    tarefas = service.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0].id == t2.id
