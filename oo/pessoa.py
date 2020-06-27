class Pessoa:

    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Osvaldo')
    print(id(p))
    print(f'Nome: {p.nome} - Idade: {p.idade}')