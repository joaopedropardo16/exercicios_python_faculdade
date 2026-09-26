# Questão 07 – Análise de Caracteres e Palavras
# O programa deverá receber uma frase e informar:
# - Quantidade total de caracteres;
# - Quantidade de letras;
# - Quantidade de números;
# - Quantidade de espaços;
# - Quantidade de palavras.
# A análise dos caracteres deverá ser realizada utilizando while.

def analisar_texto(texto):
    caracteres = len(texto)
    letras = 0
    numeros = 0
    espacos = 0

    i = 0

    while i < len(texto):
        if texto[i].isalpha():
            letras += 1
        elif texto[i].isdigit():
            numeros += 1
        elif texto[i] == " ":
            espacos += 1

        i += 1

    palavras = len(texto.split())

    return caracteres, letras, numeros, espacos, palavras


frase = input("Digite uma frase: ")

caracteres, letras, numeros, espacos, palavras = analisar_texto(frase)

print("Total de caracteres:", caracteres)
print("Quantidade de letras:", letras)
print("Quantidade de números:", numeros)
print("Quantidade de espaços:", espacos)
print("Quantidade de palavras:", palavras)