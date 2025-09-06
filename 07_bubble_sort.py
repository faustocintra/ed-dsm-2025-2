passd = comps = trocas = None   # Variáveis de estatística

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o SEGUNDO for MENOR do que o PRIMEIRO. Efetua tantas
    passadas quanto forem necessárias, até que, na última
    passada, nenhuma troca tenha sido necessária.
    """
    # Loop eterno: não sabemos antecipadamente quantas
    # passadas serão necessárias
    global passd, comps, trocas
    passd = comps = trocas = 0

    while True:
        if passd % 50 == 0: print(f"Processando passada: {passd}")

        passd += 1      # Começa nova passada

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO
        # elemento, com acesso a cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente na lista 
            # (pos + 1) for MENOR do que aquele que está
            # atrás (pos), efetuamos uma troca ente eles
            comps += 1
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                # Marcamos que houve troca na passada
                trocou = True
                trocas += 1

        # <-- CUIDADO COM A INDENTAÇÃO AQUI
        # Se não houve troca na passada (trocou ainda é False),
        # a lista está ordenada e interrompemos o loop eterno while
        if not trocou: break

######################################################################

# Caso médio
nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]
# Passadas: 9; comparações: 45; trocas: 8

# Pior caso
# nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Passadas: 10; comparações: 90; trocas: 45

# Melhor caso
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Passadas: 1; comparações: 9; trocas: 0

print("ANTES :", nums)
bubble_sort(nums)
print("DEPOIS:", nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

#####################################################################

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTE COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Trabalhando apenas com os primeiros 10000 nomes
nomes = nomes[:100000]

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()

print(nomes)

print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")
