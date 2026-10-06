# Questão 9 – Análise de Vendas
# Uma empresa registrou a quantidade de produtos vendidos durante 6 dias:
# vendas = [15, 22, 18, 30, 25, 20]
# Desenvolva um programa utilizando for para:
# • Exibir as vendas de cada dia;
# • Calcular o total de produtos vendidos;
# • Calcular a média diária de vendas;
# • Identificar os dias em que as vendas ficaram acima da média;
# • Informar o maior número de vendas registrado.

vendas = [15, 22, 18, 30, 25, 20]

total = 0

for venda in vendas:
    total += venda

media = total / len(vendas)
maior = max(vendas)

print("Vendas por dia:")
for i in range(len(vendas)):
    print(f"Dia {i+1}: {vendas[i]}")

print("\nDias acima da média:")
for i in range(len(vendas)):
    if vendas[i] > media:
        print(f"Dia {i+1}")

print(f"\nTotal: {total}")
print(f"Média: {media}")
print(f"Maior venda: {maior}")