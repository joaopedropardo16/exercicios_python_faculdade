# Questão 03 – Análise de Frequência de Palavras
# Crie um programa que receba uma frase digitada pelo usuário e utilize uma função chamada:

# A função deverá:
# 1. Converter a frase para letras minúsculas;
# 2. Separar as palavras;
# 3. Armazenar a quantidade de ocorrências de cada palavra em um dicionário;

# Professor Jean Holguim – Engenharia de Software 4
# 4. Retornar o dicionário.

def contar_palavras(frase):
    palavras = frase.lower().split()
    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


frase = input("Digite uma frase: ")

resultado = contar_palavras(frase)

for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")