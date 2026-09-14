# #Questão 8 – Pesquisa de Números
# Solicite ao usuário 10 números inteiros e armazene-os em uma lista.
# Depois de preencher a lista, utilize for para:
# • Exibir os números digitados;
# • Contar quantos são positivos;
# • Contar quantos são negativos;
# • Contar quantos são iguais a zero.
# Ao final, apresente os resultados da pesquisa.

numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

positivos = 0
negativos = 0
zeros = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

print(f"Números digitados: {numeros}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")