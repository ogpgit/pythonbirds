class Pessoa:

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    fabio = Pessoa(nome = 'Fabio Pires')
    luciano = Pessoa(fabio, nome='Luciano')
    print(id(luciano))
    print(f'Nome: {luciano.nome} - Idade: {luciano.idade}')
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome = 'Ramaho' # incluindo atributo dinâmicamente
    del luciano.filhos # deletando atributo dinâmicamente
    print(luciano.__dict__)
    print(fabio.__dict__)
    print(luciano.sobrenome)
