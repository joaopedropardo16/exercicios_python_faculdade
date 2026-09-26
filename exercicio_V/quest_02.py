# Questão 02 – Cadastro e Validação de Produtos
# Desenvolva um programa para cadastrar produtos de uma loja.
# O sistema deverá utilizar um dicionário para armazenar os produtos no seguinte formato:

# Professor Jean Holguim – Engenharia de Software 3
# O cadastro deverá continuar enquanto o usuário desejar.
# Crie uma função:

# A função deverá:
# • receber o dicionário;
# • receber o nome do produto;
# • receber o preço;
# • inserir o produto no dicionário.
# O programa não deverá aceitar preço menor ou igual a zero.
# Ao final, apresente todos os produtos cadastrados.
# continue
# print(f"{nome}: R$ {preco:.2f}")

def cadastrar_produto(produtos, nome, preco):
    produtos[nome] = preco


produtos = {}

while True:
    nome = input("Nome do produto: ")

    while True:
        preco = float(input("Preço: R$ "))
        if preco > 0:
            break
        print("Preço inválido!")

    cadastrar_produto(produtos, nome, preco)

    continuar = input("Deseja cadastrar outro produto? (S/N): ").upper()

    if continuar != "S":
        break

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")