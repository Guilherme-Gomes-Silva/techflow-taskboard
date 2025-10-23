# TechFlow TaskBoard: Sistema de Gerenciamento Ágil de Tarefas

## 📝 1. Objetivo do Projeto

Desenvolver um sistema básico de gerenciamento de tarefas, utilizando a metodologia ágil, para a startup de logística (cliente fictício), permitindo o acompanhamento do fluxo de trabalho em tempo real e a priorização de tarefas.

## 🚧 2. Escopo Inicial

O projeto se concentra na implementação de uma funcionalidade essencial: **CRUD (Create, Read, Update, Delete)** para o gerenciamento de tarefas.
* **Funcionalidades Principais:**
    * Criação de novas tarefas (título e descrição).
    * Visualização de todas as tarefas.
    * Atualização do status da tarefa (ex: 'A Fazer' para 'Concluído').
    * Exclusão de tarefas.
* **Tecnologias:** [Python/Flask ou JavaScript/Express], Pytest, GitHub Actions.

## 🚀 3. Metodologia Adotada

Adotamos o framework **Kanban** para gerenciar o fluxo de trabalho.
* **Colunas do Board:**
    1.  **A Fazer (To Do):** Tarefas priorizadas e prontas para o desenvolvimento.
    2.  **Em Progresso (In Progress):** Tarefas que estão sendo ativamente desenvolvidas ou testadas.
    3.  **Concluído (Done):** Tarefas finalizadas, revisadas e prontas para entrega.
* O fluxo de trabalho é visualizado e gerenciado através da aba **Projects** do GitHub.

## ⚙️ 4. Como Executar o Sistema

Siga os passos abaixo para baixar, instalar e executar o sistema de gerenciamento de tarefas:

1. **Clonar o repositório:**

   * Abra o terminal ou prompt de comando.
   * Digite o comando:

     ```bash
     git clone https://github.com/Guilherme-Gomes-Silva/techflow-taskboard.git
     ```
   * Isso criará uma cópia do projeto em sua máquina.

2. **Acessar a pasta do projeto:**

   ```bash
   cd techflow-taskboard
   ```

3. **Instalar o Python:**

   * Certifique-se de ter o **Python 3.11** ou superior instalado.
   * Para verificar, digite:

     ```bash
     python --version
     ```
   * Se não estiver instalado, faça o download em [https://www.python.org/downloads/](https://www.python.org/downloads/).

4. **Instalar dependências necessárias:**

   * Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.
   * No terminal, digite:

     ```bash
     pip install -r requirements.txt
     ```
   * Isso instalará automaticamente tudo que o sistema precisa para rodar.

5. **Executar o sistema:**

   * Dentro da pasta do projeto, execute:

     ```bash
     python -m src.main
     ```
   * O menu do sistema será exibido no terminal, permitindo criar, listar, atualizar e excluir tarefas.

6. **Dicas de uso:**

   * Digite o número da opção desejada para navegar pelo menu.
   * Para sair do sistema, escolha a opção `6`.
   * As tarefas são salvas automaticamente no arquivo `tarefas.json`, dentro da pasta do projeto.

## 🔄 5. Mudança de Escopo

Durante o desenvolvimento do projeto, algumas alterações foram feitas em relação à proposta inicial:

* **Usuário não implementado:**
  Inicialmente, cada usuário poderia ter várias tarefas, e cada tarefa pertenceria a um único usuário, com atributos como `id`, `nome` e `email`. Para simplificar e focar na lógica central de gerenciamento de tarefas, esta funcionalidade foi retirada.

* **Substituição do Flask por JSON:**
  A interface web via Flask não foi utilizada. Em vez disso, o sistema roda no terminal e utiliza arquivos **JSON** para armazenar as tarefas, garantindo persistência dos dados entre execuções. Isso permitiu manter toda a lógica de criação, listagem, atualização e exclusão de tarefas sem a necessidade de endpoints web.
