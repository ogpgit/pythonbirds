class Pessoa:

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(Pessoa.comprimentar(p))
    print(p.comprimentar(7))