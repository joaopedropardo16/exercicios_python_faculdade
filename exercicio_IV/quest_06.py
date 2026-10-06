#Questão 6 – Produtos e Preços
#Considere a seguinte lista:
#precos = [25.50, 40.00, 15.75, 80.00, 120.50]
#Utilizando for, desenvolva um programa que:
#• Exiba cada preço;
#• Calcule o valor total dos produtos;
#• Calcule o preço médio;
#• Identifique quais produtos possuem preço superior a R$ 50,00.
precos = [25.50, 40.00, 15.75, 80.00, 120.50]

soma = 0

for preco in precos:
    print(f"R${preco:.2f}")
    soma += preco

media = soma / len(precos)

print("\nProdutos acima de R$ 50,00:")
for preco in precos:
    if preco > 50:
        print(f"R$ {preco:.2f}")

print(f"\nValor total: R$ {soma:.2f}")
print(f"Preço médio: R$ {media:.2f}")