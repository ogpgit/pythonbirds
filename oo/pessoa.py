class Pessoa:

    def __init__(self, nome = None, idade = 36):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano', 40)
    print(id(p))
    print(Pessoa.comprimentar(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome = 'Osvaldo'
    print(p.nome)
    print(p.idade)