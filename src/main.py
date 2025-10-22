from src.services.tarefa_service import TarefaService

def exibir_menu():
    print("\n===== SISTEMA DE GERENCIAMENTO DE TAREFAS =====")
    print("Escolha uma opção:")
    print("1. Criar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Atualizar status de uma tarefa")
    print("4. Excluir uma tarefa")
    print("5. Exibir instruções de uso")
    print("6. Sair")
    print("===============================================")

def exibir_instrucoes():
    print("\n===== INSTRUÇÕES DE USO =====")
    print("1️  Criar nova tarefa → permite registrar uma tarefa com título e descrição.")
    print("2️  Listar tarefas → mostra todas as tarefas cadastradas e seus status.")
    print("3️  Atualizar status → altera o status de uma tarefa (ex: Pendente → Concluída).")
    print("4️  Excluir tarefa → remove uma tarefa pelo seu ID.")
    print(" As tarefas são salvas automaticamente em um arquivo JSON (tarefas.json).")
    print(" Status possíveis: Pendente, Em andamento, Concluída.")
    print("===============================")

def main():
    service = TarefaService()

    print("Bem-vindo(a) ao Sistema de Gerenciamento de Tarefas!")
    print("Digite o número correspondente à ação desejada.")
    exibir_instrucoes()

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ").strip()

        if opcao == "1":
            titulo = input("\nTítulo da tarefa: ").strip()
            descricao = input("Descrição da tarefa: ").strip()
            tarefa = service.criar_tarefa(titulo, descricao)
            print(f"\n Tarefa '{tarefa.titulo}' criada com sucesso! (ID: {tarefa.id})")

        elif opcao == "2":
            tarefas = service.listar_tarefas()
            if not tarefas:
                print("\n Nenhuma tarefa cadastrada ainda.")
            else:
                print("\n===== LISTA DE TAREFAS =====")
                for tarefa in tarefas:
                    print(f"[{tarefa.id}] {tarefa.titulo} - {tarefa.status} (Criada em: {tarefa.data_criacao})")
                    print(f"    Descrição: {tarefa.descricao}")
                    
                print("=============================")

        elif opcao == "3":
            try:
                id_tarefa = int(input("Digite o ID da tarefa: "))
                novo_status = input("Novo status (Pendente / Em andamento / Concluída): ").strip()
                tarefa = service.atualizar_status(id_tarefa, novo_status)
                if tarefa:
                    print(f"\n Status da tarefa '{tarefa.titulo}' atualizado para '{tarefa.status}'.")
                else:
                    print("\n Tarefa não encontrada.")
            except ValueError:
                print("\n ID inválido! Digite um número.")

        elif opcao == "4":
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
                service.excluir_tarefa(id_tarefa)
                print(f"\n  Tarefa {id_tarefa} excluída com sucesso.")
            except ValueError:
                print("\n ID inválido! Digite um número.")

        elif opcao == "5":
            exibir_instrucoes()

        elif opcao == "6":
            print("\n Saindo do sistema. Até a próxima!")
            break

        else:
            print("\n Opção inválida! Escolha uma das opções listadas.")

if __name__ == "__main__":
    main()

