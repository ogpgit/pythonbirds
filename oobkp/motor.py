"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classees:

1) Motor
2) Direção

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

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 1:
            self.velocidade -= 2
        else:
            self.velocidade = 0

if __name__ == '__main__':
    motor = Motor()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
