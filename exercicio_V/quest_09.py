# Questão 09 – Sistema de Cadastro de Clientes
# Desenvolva um sistema de cadastro de clientes utilizando lista de dicionários.
# Cada cliente deverá possuir:
# O sistema deverá permitir:
# 1. Cadastrar cliente;
# 2. Pesquisar cliente pelo nome;
# 3. Listar todos os clientes;
# 4. Encerrar o programa.
# Utilize funções para organizar as operações e while para controlar o menu.
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas.

def cadastrar_cliente(clientes):
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    clientes.append({
        "nome": nome,
        "email": email,
        "telefone": telefone
    })


def pesquisar_cliente(clientes, nome):
    for cliente in clientes:
        if cliente["nome"].lower() == nome.lower():
            return cliente

    return None


def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente)


clientes = []

while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Pesquisar cliente")
    print("3 - Listar clientes")
    print("4 - Encerrar")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_cliente(clientes)

    elif opcao == "2":
        nome = input("Nome do cliente: ")
        cliente = pesquisar_cliente(clientes, nome)

        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        listar_clientes(clientes)

    elif opcao == "4":
        break