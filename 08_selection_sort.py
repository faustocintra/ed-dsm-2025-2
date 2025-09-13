passd = comps = trocas = None      # Variáveis de estatística

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em seguuida,
    encontra o menor valor entre os elementos restantes na lista.
    Se o valor encontrado for MENOR do que o valor previamente
    selecionado, efetua a troca entre eles. Continuando, seleciona
    o segundo da lista, buscando pelo menor valor nas posições
    subsequentes. Faz a troca entre os dois valores, se necessário.
    O processo se repete até que o penúltimo elemento da lista seja
    selecionado, comparado com o último e feita a troca entre eles,
    caso preciso.
    """
    global passd, comps, trocas
    passd = comps = trocas = 0

    # Loop que vai da primeira até a PENÚLTIMA posição para
    # selecionar o elemento que será comparado com os demais
    for pos_sel in range(len(lista) - 1):
        passd += 1

        # Inicia supondo que a posição do menor valor do resto
        # da lista é aquela que está imediatamente à frente da
        # posição do valor selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a
        # pos_menor até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor que estiver na posição atual (pos) for
            # MENOR do que aquele apontado por pos_menor, ajusta
            # pos_menor para o mesmo valor que pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <-- CUIDADO COM A INDENTAÇÃO AQUI!
        # Neste ponto, já terminamos de percorrer o restante da lista e
        # sabemos a posição do menor valor que há ali. Comparamos, então,
        # os valores das posições pos_menor e pos_sel. Se o primeiro for
        # MENOR do que o segundo, efetuamos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas += 1

###########################################################################

# Caso médio
nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]
# Passadas: 9; comparações: 45; trocas: 8

# Melhor caso
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Passadas: 9; comparações: 45; trocas: 0

# Pior caso
# nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# Passadas: 9; comparações: 45; trocas: 9

print("ANTES :", nums)
selection_sort(nums)
print("DEPOIS:", nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTE COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Trabalhando apenas com os primeiros 10000 nomes
nomes = nomes[:100000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")