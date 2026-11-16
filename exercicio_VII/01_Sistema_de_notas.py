def calcular_media(notas):
    return sum(notas) / len(notas)


def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


nome = input("Digite o nome do estudante: ")

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = calcular_media(notas)
resultado = situacao(media)

print("\n--- Resultado acadêmico ---")
print(f"Estudante: {nome}")
print(f"Média: {media:.2f}")
print(f"Situação: {resultado}")