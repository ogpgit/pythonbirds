class Pessoa:

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    fabio = Pessoa(nome = 'Fabio')
    osvaldo = Pessoa(fabio, nome='Osvaldo')
    print(id(osvaldo))
    print(f'Nome: {osvaldo.nome} - Idade: {osvaldo.idade}')
    for filhos in osvaldo.filhos:
        print(filhos.nome)