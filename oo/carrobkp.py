"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classees:

1) Motor
2) Direção

O Motor terá a responsabilidade ce controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2 Método acelerar, que deverá inclrementar a velocidade ema unidade
3) Méto frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela ofecerá
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2 Método girar_a_direta
2 Método girar_a_esquerda


   N
O     L
   S

    Exemplo:
    >>> # Testando Carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frar()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
class Carro:
    pass