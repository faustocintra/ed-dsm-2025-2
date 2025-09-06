divs = comps = juncs = None         # Variáveis de estatística

def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    No processo de ordenação, este algoritmo "desmonta"
    a lista original, contendo N elementos, até obter
    N listas com apenas um elemento cada uma. Em seguida,
    utilizando a técnica de mesclagem ("merging"), "monta"
    uma nova lista, com os elementos já ordenados.
    """
    global divs, comps, juncs

    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM (SUB)LISTAS MENORES

    # Para que possa haver a divisão da lista, esta deve ter mais
    # de um elemento. Caso contrário, sai da função retornando a
    # própria lista
    if len(lista) <= 1: return lista

    # Calcula a posição do meio da lista, para fazer a divisão
    # em duas partes (aproximadamente) do mesmo tamanho
    meio = len(lista) // 2

    # Tira uma cópia (usando fatiamento) da primeira metade da lista
    sublista_esq = lista[:meio]

    # Faz o mesmo para a segunda metade
    sublista_dir = lista[meio:]

    divs += 1

    # print(f"ESQ: {sublista_esq}; DIR: {sublista_dir}")

    # Chamamos recursivamente a própria função para que ela continue
    # repartindo cada sublista em duas partes
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # PARTE 2: REMONTAGEM DA LISTA, DE FORMA ORDENADA

    # Ponteiros para percorrer as sublistas esquerda e direita
    pos_esq = pos_dir = 0

    # Inicializando duas listas vazias, na mesma linha
    ordenada, sobra = [], []

    # Percorremos as sublistas esquerda e direita, comparando seus
    # elementos e os inserindo na lista ordenada
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        # O menor elemento está na sublista esquerda
        comps += 1
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1    # Avança o ponteiro da sublista esquerda
        # O menor elemento está na sublista direita
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1    # Avança o ponteiro da sublista direita

    # <-- CUIDADO COM A INDENTAÇÃO AQUI

    # Verifica se há sobras na sublista da esquerda
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    # A sobra pode estar também na sublista da direita
    else: sobra = sublista_dir[pos_dir:]

    # O resultado final é a junção (concatenação) da lista ordenada
    # com a sobra
    juncs += 1
    return ordenada + sobra

#####################################################################

divs = comps = juncs = 0
nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]
print("ANTES: ", nums)

# O Merge Sort sempre cria uma nova lista e preserva a 
# original, desordenada
nums_ord = merge_sort(nums)

print("DEPOIS:", nums_ord)
print(f"Divisões: {divs}; comparações: {comps}; junções: {juncs}")

#####################################################################

divs = comps = juncs = 0

from time import time

import sys, tracemalloc
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTE COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Trabalhando apenas com os primeiros 10000 nomes
#nomes = nomes[:100000]

tracemalloc.start()         # Inicia a medição de memória
hora_ini = time()
nomes_ord = merge_sort(nomes)
hora_fim = time()

# Captura as informações de consumo de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(nomes_ord)

#print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")
print(f"Divisões: {divs}; comparações: {comps}; junções: {juncs}")