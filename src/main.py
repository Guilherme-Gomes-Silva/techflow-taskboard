from src.services.tarefa_service import TarefaService
from src.models.tarefa import Status

service = TarefaService()

# Criar uma tarefa
t1 = service.criar_tarefa("Estudar UML", "Revisar diagramas de classe e de uso")
print("Criada:", t1.to_dict())

# Listar todas
print("\nTarefas atuais:")
for t in service.listar_tarefas():
    print(t.to_dict())

# Atualizar status
service.atualizar_status(1, Status.CONCLUIDA)

# Excluir
# service.excluir_tarefa(1)
