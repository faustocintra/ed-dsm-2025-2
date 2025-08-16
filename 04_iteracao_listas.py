frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer (iterar) uma lista e exibir apenas
# seus elementos, usamos a estrutura for..in, como
# já visto no arquivo 02
for f in frutas:
    print(f)

print("-" * 80)

# Percorrendo a lista em ordem reversa: reversed()
for x in reversed(frutas):
    print(x)

print("-" * 80)

# No entanto, é comum precisar exibir, além do valor do
# elemento, também sua posição na lista. Nesse caso,
# devemos usar a estrutura for..in combinada com as
# funções range() e len()
print("Percurso mostrando posição e valor:")
for pos in range(len(frutas)):
    print(f"Posição {pos} => {frutas[pos]}")

print("-" * 80)

# Às vezes, é necessário percorrer a lista em ordem
# reversa, tendo acesso também às posições dos elementos.
# Para isso, usamos for..in, len() e range() com três
# parâmetros
print("Percurso inverso mostrando posição e valor:")
for p in range(len(frutas) - 1, -1, -1):
    print(f"Posição {p} => {frutas[p]}")