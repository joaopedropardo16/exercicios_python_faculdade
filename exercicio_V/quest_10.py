# Questão 10 – Sistema Integrado de Análise de Dados
# Desenvolva um programa que simule um pequeno sistema de análise de dados.
# O programa deverá receber nomes e notas de vários estudantes até que o usuário informe uma opção de
# encerramento.
# Armazene os dados utilizando uma lista de dicionários:
# Professor Jean Holguim – Engenharia de Software 8
# Crie as seguintes funções:
# O sistema deverá apresentar um menu:
# Considere aprovado o estudante com nota maior ou igual a 7.0.
# Utilize while para controlar a execução do sistema e funções para organizar as operações.

def cadastrar_estudante(estudantes):
    nome = input("Nome: ")
    nota = float(input("Nota: "))

    estudantes.append({
        "nome": nome,
        "nota": nota
    })


def calcular_media(estudantes):
    if not estudantes:
        return 0

    soma = 0

    for aluno in estudantes:
        soma += aluno["nota"]

    return soma / len(estudantes)


def maior_nota(estudantes):
    if not estudantes:
        return None

    return max(estudantes, key=lambda aluno: aluno["nota"])


def listar_aprovados(estudantes):
    for aluno in estudantes:
        if aluno["nota"] >= 7:
            print(aluno["nome"], "-", aluno["nota"])


estudantes = []

while True:
    print("\n1 - Cadastrar estudante")
    print("2 - Exibir média da turma")
    print("3 - Exibir estudante com maior nota")
    print("4 - Listar aprovados")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_estudante(estudantes)

    elif opcao == "2":
        print(f"Média da turma: {calcular_media(estudantes):.2f}")

    elif opcao == "3":
        aluno = maior_nota(estudantes)

        if aluno:
            print(f"{aluno['nome']} - {aluno['nota']}")

    elif opcao == "4":
        listar_aprovados(estudantes)

    elif opcao == "5":
        break