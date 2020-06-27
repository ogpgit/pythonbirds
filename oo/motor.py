"""
A classe Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2 Método acelerar, que deverá inclrementar a velocidade ema unidade
3) Méto frear que deverá decrementar a velocidade em duas unidades

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
"""
class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1

if __name__ == '__main__':
    m1 = Motor()
    m1.velocidade = 2
    print(m1.velocidade)
    m1.acelerar()
    print(m1.velocidade)
#    print(m1.acelerar())
#    print(m1.velocidade)
