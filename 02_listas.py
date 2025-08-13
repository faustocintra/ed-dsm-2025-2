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

print("-" * 80)     # Traço separador

# 2) INSERÇÃO DE UM NOVO ELEMENTO NA LISTA
print("Lista de frutas, ANTES DA INSERÇÃO:", frutas)
print("Lista de números, ANTES DA INSERÇÃO:", nums)

# Inserindo um novo item ao FINAL da lista: append()
frutas.append("maracujá")
nums.append(19)

print("Lista de frutas, APÓS A INSERÇÃO:", frutas)
print("Lista de números, APÓS A INSERÇÃO:", nums)

print("-" * 80)     # Traço separador

# Inserindo um novo elemento NA POSIÇÃO ESPECIFICADA: insert()
# Parâmetros:
# 1º ~> a posição onde será feita a inserção (a contagem COMEÇA EM ZERO!!)
# 2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na PRIMEIRA posição (posição 0)
frutas.insert(0, "melancia")
print("Lista de frutas após inserir 'melancia' na posição 0:")
print(frutas)

# Inserindo um novo elemento na QUARTA posição (posição 3)
frutas.insert(3, "amora")
print("Lista de frutas após inserir 'amora' na posição 3:")
print(frutas)

print("-" * 80)     # Traço separador

# 3) ACESSANDO VALORES DA LISTA POR SUA POSIÇÃO
print("Elemento da QUINTA posição:   ", frutas[4])
print("Elemento da PRIMEIRA posição: ", frutas[0])
print("Elemento da ÚLTIMA posição:   ", frutas[-1])
print("Elemento da PENÚLTIMA posição:", frutas[-2])

print("-" * 80)     # Traço separador

# 4) SUBSTITUINDO VALORES EXISTENTES
print("Lista de frutas antes das substituições:")
print(frutas)

# Substituindo o valor da posição 3 (QUARTA posição)
frutas[3] = "framboesa"
# Substituindo o valor da posição 0 (PRIMEIRA posição)
frutas[0] = "pitanga"
# Substituindo o valor da posição -1 (ÚLTIMA posição)
frutas[-1] = "melão"

print("Lista de frutas após as substituições:")
print(frutas)

print("-" * 80)     # Traço separador

# 5) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()
print("Quantidade de elementos da lista de frutas: ", len(frutas))
print("Quantidade de elementos da lista de números:", len(nums))

print("-" * 80)     # Traço separador

# 6) REMOÇÃO DE UM ELEMENTO DA LISTA
print("Lista de frutas, ANTES das remoções:")
print(frutas)

# Removendo o ÚLTIMO elemento da lista: pop() (SEM parâmetro)
print("Removendo o último elemento...")
removido = frutas.pop()
print("Elemento removido:", removido)
print("Lista de frutas, após a remoção do último elemento:")
print(frutas)

# Removendo o elemento POR SUA POSIÇÃO: pop() (COM parâmetro)
print("Removendo o elemento da posição 4...")
removido = frutas.pop(4)
print("Elemento removido:", removido)
print("Lista de frutas, após a remoção do elemento da posição 4:")
print(frutas)

# Removendo o elemento POR SEU VALOR: remove()
print("Removendo o elemento 'manga'...")
frutas.remove("manga")
print("Lista de frutas, após a remoção do elemento 'manga':")
print(frutas)

print("-" * 80)     # Traço separador

# 7) AUMENTANDO UMA LISTA COM ELEMENTOS DE OUTRA LISTA: extend()
mais_frutas = ["carambola", "pera", "acerola", "jabuticaba", "caqui"]
frutas.extend(mais_frutas)
print("Lista de frutas estendida com mais frutas:")
print(frutas)
