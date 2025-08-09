"""
LISTA é uma estrutura de dados nativa da linguagem
Python. Ela permite que uma série de valores seja
associada a uma única variável.
"""

# Lista de strings
frutas = ["maçã", "morango", "laranja", "uva", "manga", "goiaba"]

# Lista de números
nums = [3, 10, -7, 12.8, -0.5, 4, 22]

# Lista com valores de vários tipos (pouco comum)
mistureba = ["Pafúncio", 37, 1.81, 79, True]

#### OPERAÇÕES SOBRE LISTAS ####

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um dos seus
# itens e fazer algo com ele. Nos exemplos a seguir, vamos
# dar print() em cada uma das frutas da lista
for x in frutas:
    print(f"A fruta da vez é {x}")

print("-" * 80)     # Traço separador

# Percorrendo a lista de números e exibindo o seu valor e
# também o resultado de sua elevação ao quadrado
for num in nums:
    print(f"{num} => {num ** 2}")

