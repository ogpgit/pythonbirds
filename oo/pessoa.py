class Pessoa:
    olhos = 2 # Atributo de classe

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 4

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        return f'{super().cumprimentar()}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome ='Renzo')
    luciano = Homem(renzo, nome='Luciano')#
    # print(id(luciano))
    # print(f'Nome: {luciano.nome} - Idade: {luciano.idade}')
    # for filhos in luciano.filhos:
   #      print(filhos.nome)
   #  luciano.sobrenome = 'Ramaho' # incluindo atributo dinâmicamente
   #  del luciano.filhos # deletando atributo dinâmicamente

    luciano.olhos = 1
    print(luciano.__dict__)
    print(renzo.__dict__)

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

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Homem))
    print(isinstance(pessoa, Pessoa))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    # fabio.olhos = 4
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
