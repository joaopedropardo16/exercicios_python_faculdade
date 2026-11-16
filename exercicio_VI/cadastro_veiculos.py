class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.__ano = ano

    # Encapsulamento
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano > 0:
            self.__ano = novo_ano
        else:
            print("Ano inválido!")

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


# Herança
class Carro(Veiculo):
    def abrir_porta(self):
        print("O carro abriu a porta!")

    # Polimorfismo
    def exibir_dados(self):
        print("\n--- CARRO ---")
        super().exibir_dados()


class Moto(Veiculo):
    def empinar(self):
        print("A moto está empinando!")

    # Polimorfismo
    def exibir_dados(self):
        print("\n--- MOTO ---")
        super().exibir_dados()


# Sistema de cadastro
veiculos = []

while True:
    print("\n===== CADASTRO DE VEÍCULOS =====")
    print("1 - Cadastrar carro")
    print("2 - Cadastrar moto")
    print("3 - Listar veículos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        marca = input("Digite a marca: ")
        modelo = input("Digite o modelo: ")
        ano = int(input("Digite o ano: "))

        carro = Carro(marca, modelo, ano)
        veiculos.append(carro)

        print("Carro cadastrado com sucesso!")

    elif opcao == "2":
        marca = input("Digite a marca: ")
        modelo = input("Digite o modelo: ")
        ano = int(input("Digite o ano: "))

        moto = Moto(marca, modelo, ano)
        veiculos.append(moto)

        print("Moto cadastrada com sucesso!")

    elif opcao == "3":
        if len(veiculos) == 0:
            print("Nenhum veículo cadastrado.")
        else:
            for veiculo in veiculos:
                veiculo.exibir_dados()

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")