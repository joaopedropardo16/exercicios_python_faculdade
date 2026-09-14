#Questão 7 – Temperaturas da Semana
#Crie uma lista contendo as temperaturas registradas durante 7 dias.
#Exemplo:
#temperaturas = [28, 30, 27, 31, 29, 32, 26]
#Utilizando for, o programa deverá:
#1. Exibir todas as temperaturas;
#2. Calcular a temperatura média;
#3. Identificar a maior temperatura;
#4. Identificar a menor temperatura;
#5. Informar quantos dias apresentaram temperatura acima da média.

temperaturas = [28, 30, 27, 31, 29, 32, 26]

soma = 0

for temperatura in temperaturas:
    soma += temperatura

media = soma / len(temperaturas)

maior = max(temperaturas)
menor = min(temperaturas)

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1

print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Dias acima da média: {acima_media}")