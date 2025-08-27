# Variável global para a contagem de comparações
comps = None

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dada uma lista, que DEVE ESTAR PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas no lado onde o
    valor de busca poderia estar. Novas subdivisões são
    feitas até que se encontre o valor de busca ou que
    reste apenas uma sublista vazia, quando então se
    conclui que o valor de busca não existe na lista.
    """
    # Avisando à função que queremos usar a variável global
    global comps
    comps = 0   # Zerando o valor para começar a contar

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        # Calculando a posição do meio da lista
        # O operador // significa divisão inteira
        meio = (ini + fim) // 2

        # Verifica se o valor que está no meio da lista é
        # igual ao valor de busca. Em caso afirmativo, 
        # retornamos a posição do meio, pois o valor de busca
        # foi encontrado
        if val == lista[meio]: 
            comps += 1
            return meio

        # Senão, se o valor de busca é MENOR do que o valor do
        # meio, move o ponteiro do fim para a posição anterior
        # à do meio e reinicia a busca na metade ESQUERDA da
        # (sub)lista
        elif val < lista[meio]: 
            comps += 2
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR do que o valor
        # do meio, move o ponteiro do início para a posição
        # seguinte à do meio e reinicia a busca na metade
        # DIREITA da lista
        else: 
            comps += 2
            ini = meio + 1

    # <-- CUIDADO COM A INDENTAÇÃO AQUI
    # Se chegamos a este ponto, é porque o valor de busca não
    # existe na lista
    return -1

#############################################################

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

vals = [30, 4, -3]

for v in vals:
    pos = busca_binaria(nums, v)
    if pos >= 0:
        print(f"Elemento {v} encontrado na posição {pos}, comparações: {comps}.")
    else:
        print(f"Elemento {v} não foi encontrado, pois a busca retornou o valor {pos}, comparações: {comps}.")

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
    pos = busca_binaria(nomes, n)
    hora_fim = time()
    if pos >= 0:
        print(f"Nome {n} encontrado na posição {pos}, comparações: {comps}.")
    else:
        print(f"Nome {n} não encontrado, comparações {comps}.")

    print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")