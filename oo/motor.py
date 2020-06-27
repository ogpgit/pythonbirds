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

    def __init__(self):
        pass

if __name__ == '__main__':
    print(Motor.velocidade)
    #m = Motor()
    # print(m.velocidade)

     #print(Motor.velocidade)