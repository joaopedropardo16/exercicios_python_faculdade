#Questão 2 – Tabuada
#Desenvolva um programa que solicite ao usuário um número inteiro e utilize for para apresentar a tabuada desse número de 1 a 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")