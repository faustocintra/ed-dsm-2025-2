"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem
Python capaz de armazenar múltiplos valores em uma única
variável, por meio de pares de chave-valor (key-value).
Um dicionário é delimitado entre chaves {}. Diferentemente
da lista, que tem posições numeradas, o dicionário possui
posições NOMEADAS. Cada uma das posições nomeadas de um
dicionário (ou seja, cada par de chave-valor) é chamada de
propriedade.
"""
# Um dicionário com dados que representam uma pessoa.
# As chaves são sempre do tipo string.
# Os valores podem ser de qualquer tipo.
pessoa = {
    # "chave": valor
    "nome": "Orozimbo Oliveira Osório",             # string
    "sexo": "M",                                    # string
    "idade": 72,                                    # número inteiro
    "peso": 76,                                     # número inteiro
    "altura": 1.77,                                 # número fracionário
    "aposentado": True,                             # booleano
    "filhos": ["Zeferina", "Adamastor", "Gercina"]  # lista
}

# Acessando o valor das propriedades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("É aposentado?", pessoa["aposentado"])

print('-' * 80)     # Traço separador

# Calculando o IMC (Índice de Massa Corporal)
imc = pessoa["peso"] / pessoa["altura"] ** 2

print(f"O IMC de {pessoa["nome"]} é {imc}.")

print('-' * 80)     # Traço separador

#############################################################

# Usando dicionários para representar formas geométricas

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 3,
    "tipo": "T"     # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3.5,
    "tipo": "E"     # Elipse/círculo
}

# Valor de propriedade fora do tipo esperado
# forma4 = {
#     "base": "batata",
#     "altura": 14,
#     "tipo": "T"
# }

# Nome de propriedade inválido para a função calc_area()
forma4 = {
    "base": 20,
    "legume": 12,
    "tipo": "E"
}

from math import pi

def calc_area(forma):
    """
    Função que calcula a área de uma forma geométrica, dados a
    base, a altura e o tipo, passados como propriedade de um
    dicionário
    """
    match forma["tipo"]:
        case "R":       # Retângulo
            return forma["base"] * forma["altura"]
        case "T":       # Triângulo
            return forma["base"] * forma["altura"] / 2
        case "E":       # Elipse/círculo
            return (forma["base"] / 2) * (forma["altura"] / 2) * pi
        case _:         # Forma inválida / não reconhecida
            return None
        
# <-- CUIDADO COM A INDENTAÇÃO AQUI

# Testes com a função calc_area()

formas = [forma1, forma2, forma3, forma4]

for forma in formas:
    print(f"Base: {forma["base"]}; altura: {forma["altura"]}; tipo: {forma["tipo"]}; área: {calc_area(forma)}")