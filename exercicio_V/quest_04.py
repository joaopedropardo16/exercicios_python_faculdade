# Questão 04 – Sistema de Notas dos Estudantes
# Desenvolva um sistema para registrar estudantes e suas respectivas notas.
# Utilize um dicionário para armazenar os dados:

# Crie uma função:

# A função deverá retornar a média do estudante.
# O sistema deverá permitir cadastrar vários estudantes utilizando while.
# Ao final, apresente:
# • Nome;
# • Média;
# • Situação.
# Considere:
# • Média maior ou igual a 7 → Aprovado;

# Professor Jean Holguim – Engenharia de Software 5
# • Média entre 5 e 6.9 → Recuperação;
# • Média menor que 5 → Reprovado.

def calcular_media(notas):
    return sum(notas) / len(notas)


estudantes = {}

while True:
    nome = input("Nome do estudante: ")

    notas = []
    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    estudantes[nome] = notas

    continuar = input("Cadastrar outro estudante? (S/N): ").upper()

    if continuar != "S":
        break

print("\nResultado:")

for nome, notas in estudantes.items():
    media = calcular_media(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 20)