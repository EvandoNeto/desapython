
import unittest
from main import pedir_dados

teste = pedir_dados()

class Testes(unittest.TestCase):

    def teste_nome_limpo(self):
        self.assertFalse(teste.nome == '','Campo NOME vazio')

    def teste_idade(self):
        self.assertGreaterEqual(teste.idade,0,'Campo IDADE não pode ser menor zero')

    def teste_cidade_limpo(self):
        self.assertFalse(teste.cidade == '','Campo CIDADE vazio')

    def teste_Estado_limpo(self):
        self.assertFalse(teste.estado == '','Campo ESTADO vazio')

    def teste_idade_limpo(self):
        self.assertFalse(teste.idade == '','Campo IDADE vazio')

    def teste_sexo_limpo(self):
        self.assertFalse(teste.sexo == '','Campo SEXO vazio')

    def testa_sexo(self):
        self.assertTrue(teste.sexo.__eq__("M") or teste.Sexo.__eq__("F") or teste.sexo.__eq__("m") or teste.Sexo.__eq__("f"), "Campo SEXO não identificado")

if __name__ == '__main__':
    unittest.main()
