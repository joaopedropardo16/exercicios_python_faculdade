#Questão 5 – Cadastro de Nomes
#Crie uma lista contendo 8 nomes de estudantes.
#Utilizando for, o programa deverá:
#• Exibir todos os nomes;
#• Exibir os nomes que possuem mais de 6 caracteres;
#• Informar a quantidade de nomes que atendem a esse critério.
#Utilize a função len() para verificar a quantidade de caracteres de cada nome.

nomes = ["Carlos","Mariana","Pedro","Fernanda","Lucas","Gabriela","Joao","Beatriz"]

quantidade = 0

print("Todos os nomes:")
for nome in nomes:
    print(nome)

print("\nNomes com mais de 6 caracteres:")
for nome in nomes:
    if len(nome) > 6:
        print(nome)
        quantidade += 1

print("Quantidade:", quantidade)