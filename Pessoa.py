
class Pessoa:
    def __init__(self,nome,idade,sexo,cidade,estado):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.estado = estado

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_nome(self, idade):
        self.__idade = idade

    def get_sexo(self):
        return self.__sexo

    def set_nome(self, sexo):
        self.__sexo = sexo

    def get_cidade(self):
        return self.__cidade

    def set_nome(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado

    def set_nome(self, estado):
        self.__estado = estado


if __name__ == "__main__":
    pessoa1 = Pessoa('Neto','19', 'M', 'Fotaleza', 'Ceará')
    print(pessoa1.nome,",", pessoa1.idade,",", pessoa1.sexo,",", pessoa1.cidade,",",pessoa1.estado)