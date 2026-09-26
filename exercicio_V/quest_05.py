# Questão 05 – Validador de Senha
# Crie um programa que solicite ao usuário uma senha e utilize uma função chamada:
# A senha será considerada válida somente se possuir:
# • Pelo menos 8 caracteres;
# • Pelo menos uma letra maiúscula;
# • Pelo menos uma letra minúscula;
# • Pelo menos um número.
# O programa deverá utilizar while para continuar solicitando uma nova senha até que uma senha válida seja
# informada.

def validar_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True

    return tem_maiuscula and tem_minuscula and tem_numero


while True:
    senha = input("Digite uma senha: ")

    if validar_senha(senha):
        print("Senha válida!")
        break

    print("Senha inválida. Tente novamente.")