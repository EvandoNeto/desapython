
from Pessoa import Pessoa

def pedir_dados():
    nome = input('Escreva seu nome: ')
    idade = input('Escreva sua idade: ')
    sexo = input('Qual seu sexo: ')
    cidade = input('Qual o nome da Cidade onde você mora: ')
    estado = input('Qual o nome do Estado (UF) onde você mora: ')
    return Pessoa(nome, idade, sexo, cidade, estado)

if __name__ == "__main__":
    pedir_dados()