# Questão 08 – Menu de Sistema com Funções
# Desenvolva um sistema com menu interativo utilizando while.
# O sistema deverá apresentar:
# As tarefas deverão ser armazenadas em uma lista.
# Crie funções para:
# Professor Jean Holguim – Engenharia de Software 7
# O sistema deverá continuar executando até que o usuário escolha a opção 4.

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i} - {tarefa}")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    if tarefas:
        indice = int(input("Número da tarefa: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)


tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa(tarefas)
    elif opcao == "2":
        listar_tarefas(tarefas)
    elif opcao == "3":
        remover_tarefa(tarefas)
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")