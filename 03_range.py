"""
range() é uma função da linguagem Python que gera uma
série (faixa) de números. É muito usada em associação
com listas e com a instrução "for".
"""

# 1) range() com *UM* PARÂMETRO
#    Gera uma sequência numérica que SEMPRE começa em
#    0 (zero) e vai até o valor do parâmetro - 1
for num in range(10):
    print(num)

print("-" * 80)

# 2) range() com *DOIS* PARÂMETROS
#    1º parâmetro: valor inicial da sequência (inclusive)
#    2º parâmetro: valor final da sequência (EXCLUSIVE)
for x in range(10, 18):
    print(x)

print("-" * 80)

# 3) range() com *TRÊS* PARÂMETROS
#    1º: valor inicial (inclusive)
#    2º: valor final (EXCLUSIVE)
#    3º: valor do passo (intervalo entre um número e o seguinte)
for n in range(0, 22, 3):
    print(n)

print("-" * 80)

# 4) range() com passo negativo (CONTAGEM REGRESSIVA)
for k in range(10, 0, -1):
    print(k)