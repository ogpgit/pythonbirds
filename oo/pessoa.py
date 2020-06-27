class Pessoa:
    olhos = 2 # Atributo de classe

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 4

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    fabio = Pessoa(nome = 'Fabio Pires')
    luciano = Pessoa(fabio, nome='Luciano')#
    # print(id(luciano))
    # print(f'Nome: {luciano.nome} - Idade: {luciano.idade}')
    # for filhos in luciano.filhos:
   #      print(filhos.nome)
   #  luciano.sobrenome = 'Ramaho' # incluindo atributo dinâmicamente
   #  del luciano.filhos # deletando atributo dinâmicamente

    # luciano.olhos = 1
    # print(luciano.__dict__)
    # print(fabio.__dict__)
    # print(luciano.sobrenome)

    # print(id(Pessoa.olhos))
    # print(id(luciano.olhos))
    # print(id(fabio.olhos))
    print(Pessoa.olhos)
    # print(luciano.olhos)

    # Chamada de método de classe @staticmethod
    # print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    # Chamada de método de classe para acessar dados da própria classe @classmethod
    # print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

