#Questão 1 – Números de 1 a 20 
#Desenvolva um programa em Python que utilize a estrutura for para percorrer os números de 1 a 20
#O programa deverá:
#• Exibir todos os números;
#• Identificar quais são pares;
#• Apresentar a quantidade de números pares encontrados.

quantidade_pares = 0

for i in range(1, 21):
    if i % 2 != 0:
     print(i)
    else:
     print(f"{i} (Par)")
     quantidade_pares += 1

print("Quantidade de números pares:", quantidade_pares)