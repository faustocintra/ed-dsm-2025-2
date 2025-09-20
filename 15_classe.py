"""
Classe é uma estrutura de dados que representa simultaneamente
dados e algoritmos. Uma classe pode ser comparada a uma
"assadeira" com a qual se pode produzir diferentes tipos de
iguarias assadas, variando os "ingredientes" (dados) da receita
e o "modo de fazer" (algoritmos). Apesar dessas variações,
todos os objetos criados a partir de uma mesma classe terão
sempre algumas características comuns, impressas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classe em Python seguem o formato
    PascalCase (primeira letra de cada palavra em maiúscula).
    Uma classe pode ter, dentro de si, tanto dados como funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é invocada sempre que se tenta criar um
    novo objeto a partir da classe. Essa função especial é
    conhecida como MÉTODO CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS. O primeiro 
       parâmetro de todo método é sempre "self", que representa
       o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        # Validamos os valores de base, altura e tipo
        # e só permitimos a criação do objeto caso
        # eles sejam válidos

        if type(base) not in [int, float] or base <= 0:
            raise Exception("ERRO: 'base' deve ser numérica e maior do que zero.")
        
        if type(altura) not in [int, float] or altura <= 0:
            raise Exception("ERRO: 'altura' deve ser numérica e maior do que zero.")
        
        if tipo not in ["R", "T", "E"]:
            raise Exception("ERRO: 'tipo' deve ser 'R', 'T' ou 'E'.")
        
        # Se chegamos até aqui, os dados estão OK, e podemos armazená-los
        # em atributos
        self.base = base
        self.altura = altura
        self.tipo = tipo

##########################################################################

forma1 = FormaGeometrica(12, 14, "R")
print(forma1)

forma2 = FormaGeometrica(10, 4.5, "X")
print(forma2)