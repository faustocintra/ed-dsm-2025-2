def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô (na
    nossa implementação, será o último) e, na primeira
    passada, divide a lista, a partir da posição final do
    pivô, em uma sublista à esquerda, contendo apenas
    valores menores do que o pivô, e outra sublista à
    direita, compreendendo apenas valores maiores do que
    o pivô. Em seguida, recursivamente, repete o processo
    para cada uma das sublistas, até que toda a lista
    esteja ordenada.
    """
    # Quando o valor do parâmetro "fim" não tiver sido
    # informado, atribuímos a ele o valor da última posição
    # da lista
    if fim is None: fim = len(lista) - 1

    # Para que seja possível proceder à ordenação, é
    # necessário que a faixa delimitada pelos parâmetros
    # "ini" e "fim" contenha, pelo menos, DOIS elementos.
    # Caso não seja essa a situação, saímos da função sem
    # fazer nada
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim     # O pivô será o último elemento
    div = ini - 1   # O divisor inicia uma posição antes de "ini"

    # Percorre a lista da posição "ini" até a posição "fim" - 1
    for pos in range(ini, fim):
        # Se o elemento da posição "pos" for MENOR do que o
        # elemento da posição "pivot", chega "div" uma posição
        # à frente e promove a troca entre os elementos das
        # posições "div" e "pos"
        if lista[pos] < lista[pivot]:
            div += 1    # Avança o divisor
            # Efetua a troca apenas se as posições de 
            # "pos" e "div" forem distintas
            if pos != div:
                lista[pos], lista[div] = lista[div], lista[pos]

    # <-- CUIDADO COM A INDENTAÇÃO AQUI
    # Após o loop "for" terminar, "div" deve avançar ainda
    # uma posição
    div += 1

    # Comparamos os elementos das posições "pivot" e "div" entre
    # si e, caso o primeiro seja MENOR do que o segundo, efetuamos
    # a troca entre eles
    if lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]

    # Neste momento, todos os elementos à esquerda do pivô são
    # MENORES do que ele, e todos os elementos à sua direita
    # são MAIORES do que ele.

    # Chamamos recursivamente a função para repetir o processo
    # para as sublistas esquerda e direita
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

###################################################################