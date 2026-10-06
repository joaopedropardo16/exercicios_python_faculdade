# Questão 10 – Sistema de Análise de Dados
# Desenvolva um programa que solicite ao usuário 10 números inteiros e armazene os valores em uma lista.
# Utilizando for, o programa deverá realizar uma análise completa dos dados:
# • Exibir todos os números armazenados;
# • Calcular a soma dos valores;
# • Calcular a média;
# • Identificar o maior valor;
# • Identificar o menor valor;
# • Contar quantos números são pares;
# • Contar quantos números são ímpares;
# • Exibir os números que estão acima da média.

numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

maior = max(numeros)
menor = min(numeros)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n===== RELATÓRIO =====")
print(f"Quantidade de números: {len(numeros)}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

print("\nNúmeros acima da média:")
for numero in numeros:
    if numero > media:
        print(numero)

print("=====================")