class Pessoa2: #Substantivos
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome #Substantivos
        self.idade = idade #Substantivos

    def dirigir(self, veiculo: str) -> None: #Verbos
        print(f'Estou dirigindo um(a) {veiculo}')

    def cantar(self): #Verbos
        print('Blábláblá')

    def apresentar_idade(self) -> int: #Verbos
        return self.idade