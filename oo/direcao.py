"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classees:

1) Motor
2) Direção

A classe Direção terá a responsabilidade de controlar a direção. Ela ofecerá
os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2 Método girar_a_direta
2 Método girar_a_esquerda

   N
O     L
   S

    Exemplo:
    >>> # Testando a Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
"""
