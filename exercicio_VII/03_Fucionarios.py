class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def bonus(self):
        return self.salario * 0.20


# Criando os objetos
funcionarios = [
    Funcionario("Pedro", 3000.00),
    Gerente("Mariana", 5000.00)
]

# Exibindo os bônus
for funcionario in funcionarios:
    print(f"Nome: {funcionario.nome}")
    print(f"Bônus: R$ {funcionario.bonus():.2f}")
    print()