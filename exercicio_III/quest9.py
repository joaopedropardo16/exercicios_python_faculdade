idade = int(input("Informe sua idade: "))

if idade >= 60:
    print("Idoso")
elif idade >= 18:
    print("Adulto")
elif idade >= 13:
    print("Adolescente")
else:
    print("Criança")