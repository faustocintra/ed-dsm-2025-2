def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    No processo de ordenação, este algoritmo "desmonta"
    a lista original, contendo N elementos, até obter
    N listas com apenas um elemento cada uma. Em seguida,
    utilizando a técnica de mesclagem ("merging"), "monta"
    uma nova lista, com os elementos já ordenados.
    """
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

    print(f"ESQ: {sublista_esq}; DIR: {sublista_dir}")

    # Chamamos recursivamente a própria função para que ela continue
    # repartindo cada sublista em duas partes
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

#####################################################################

nums = [7, 0, 6, 8, 1, 3, 9, 4, 2, 5]

nums_ord = merge_sort(nums)