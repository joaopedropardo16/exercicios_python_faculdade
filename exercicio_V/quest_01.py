#Questão 01 – Sistema de Autenticação
# Desenvolva um sistema de autenticação utilizando while e funções.
# O programa deverá solicitar um usuário e uma senha. O usuário terá no máximo 3 tentativas para informar
# corretamente:
# Crie uma função chamada autenticar(usuario, senha) que retorne True quando os dados estiverem corretos e
# False caso contrário.
# Ao final:
# • Se o usuário acertar, apresente uma mensagem de acesso autorizado.
# • Se exceder 3 tentativas, apresente uma mensagem informando que o acesso foi bloqueado.


def autenticar(usuario, senha):
    return usuario == "admin" and senha == "1234"


tentativas = 0

while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if autenticar(usuario, senha):
        print("Acesso autorizado!")
        break

    tentativas += 1
    print("Usuário ou senha incorretos.")

if tentativas == 3:
    print("Acesso bloqueado.")