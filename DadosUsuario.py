
def pedir_dados():
    nome = input('Escreva seu nome: ')
    idade = input('Escreva sua idade: ')
    sexo = input('Qual seu sexo: ')
    cidade = input('Qual o nome da Cidade onde você mora: ')
    estado = input('Qual o nome do Estado (UF) onde você mora: ')
    return {'nome': nome,'idade':idade,'sexo':sexo,'cidade':cidade, 'estado':estado}

print(pedir_dados())