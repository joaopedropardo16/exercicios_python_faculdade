#Questão 4 – Lista de Notas
#Uma turma possui as seguintes notas:
#notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
#Utilizando for, desenvolva um programa que:
#1. Percorra a lista;
#2. Exiba cada nota;
#3. Calcule a média da turma;
#4. Informe quantos estudantes obtiveram nota maior ou igual a 7.0.

notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]

soma = 0
aprovados = 0

for nota in notas:
    print(nota)
    soma += nota

    if nota >= 7.0:
        aprovados += 1

media = soma / len(notas)

print(f"Média: {media}")
print(f"Alunos com nota >= 7.0: {aprovados}")