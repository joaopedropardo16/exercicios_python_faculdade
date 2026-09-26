# Questão 06 – Carrinho de Compras
# Desenvolva um sistema de carrinho de compras utilizando lista e dicionário.
# Cada produto deverá possuir:
# • Nome;
# • Quantidade;
# • Preço.
# Exemplo:

# Os produtos deverão ser armazenados em uma lista.
# Crie uma função:

# Professor Jean Holguim – Engenharia de Software 6
# que percorra os produtos e calcule o valor total da compra.
# O sistema deverá utilizar while para permitir o cadastro de vários produtos.

# O programa deverá receber uma frase e informar:
# - Quantidade total de caracteres;
# - Quantidade de letras;
# - Quantidade de números;
# - Quantidade de espaços;
# - Quantidade de palavras.
# A análise dos caracteres deverá ser realizada utilizando while.

def calcular_total(carrinho):
    total = 0

    for produto in carrinho:
        total += produto["quantidade"] * produto["preco"]

    return total


carrinho = []

while True:
    nome = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    carrinho.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    })

    continuar = input("Adicionar outro produto? (S/N): ").upper()

    if continuar != "S":
        break

print(f"Valor total: R$ {calcular_total(carrinho):.2f}")