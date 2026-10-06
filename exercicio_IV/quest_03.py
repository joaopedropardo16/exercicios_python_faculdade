#Questão 3 – Soma dos Números
#Crie um programa que utilize for para percorrer os números de 1 a 50 e calcular:
#• A soma de todos os números;
#• A soma somente dos números pares;
#• A soma somente dos números ímpares.
#Apresente os três resultados ao final da execução.

soma_total = 0
soma_pares = 0
soma_impares = 0

for numero in range(1, 51):
    soma_total += numero

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f"Soma total: {soma_total}")
print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")