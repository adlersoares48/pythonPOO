class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf #Caracteristica privada, somente acessada pela classe

    def correr(self):
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
            print(f'Bebendo {bebida}')
        else:
            print(f'Bebendo {bebida}')

    def __apresentar_documento(self): #Encapsulamento privado (apenas utilizado na classe)
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', '32 anos', '111222333')

ronaldo.beber('cerveja')