
# VÁRIAS RESPONSABILIDADES:
'''
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print(f'Cadastrar o usuário {nome}, idade {idade} anos')

        else:
            print('Dados Inválidos')
'''

# SOLID -- RESPONSABILIDADE UNICA
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print(f'Cadastrar o usuário {nome}, idade {idade} anos')

    def __indicar_erro(self) -> None:
        print('Dados Inválidos')

sis = SistemaCadastral()
sis.cadastrar('Adler', 25)