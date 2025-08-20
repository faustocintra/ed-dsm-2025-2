def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista,
    procurando por val.
    Se val for encontrado, retorna a posição de val na
    lista.
    Caso contrário, retorna o valor convencional -1.
    """
    # Percorre a lista do início ao fim, usando range()
    # e len(), porque é necessário ter acesso às posições
    # dos elementos
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos

    # <-- CUIDADO COM A INDENTAÇÃO AQUI
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1

##############################################################

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

vals = [30, 4, -3]

for v in vals:
    pos = busca_sequencial(nums, v)
    if pos >= 0:
        print(f"Elemento {v} encontrado na posição {pos}.")
    else:
        print(f"Elemento {v} não foi encontrado, pois a busca retornou o valor {pos}.")

print('-' * 80)

###############################################################

# TESTE COM 1M+ DE NOMES

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

from data.nomes_completos import nomes

buscas = [
    "EDSON PEREIRA",
    "MARIA FERREIRA",
    "VALDIR SILVA",
    "GILCINEIA GARCIA"
]

for n in buscas:
    hora_ini = time()
    pos = busca_sequencial(nomes, n)
    hora_fim = time()
    if pos >= 0:
        print(f"Nome {n} encontrado na posição {pos}.")
    else:
        print(f"Nome {n} não encontrado.")

    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")