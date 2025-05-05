#1
def repete_string(msg,qtd):
    '''
    Multiplica uma string num determinado n° de vezes
    str, int => str
    '''
    return msg*qtd

#2
import math as m
def distancia_pontos(t1,t2):
    '''
    Retorna a distância entre dois pontos no espaço 2d
    tuple, tuple => float
    '''
    xa, ya = t1
    xb, yb = t2
    return m.sqrt((xa-xb)**2+(ya-yb)**2)

#3
def distancia_pontos_3d(t1,t2):
    '''
    Retorna a distância entre dois pontos no espaço 3d
    tuple, tuple => float
    '''
    xa, ya, za = t1
    xb, yb, zb = t2
    return m.sqrt((xa-xb)**2+(ya-yb)**2+(za-zb)**2)

#4
def area_triangulo(t1,t2,t3):
    '''
    A função retorna a área do triângulo no espaço 2d
    tuple, tuple, tuple => float
    ou caso a ==0
    tuple, tuple, tuple => str
    '''
    x1, y1 = t1
    x2, y2 = t2
    x3, y3 = t3
    area = 0.5*abs(((x1*y2)+(y1*x3)+(x2*y3))-((x3*y2)+(y3*x1)+(x2*y1)))
    if area ==0:
        return "Erro: os pontos não formam um triângulo"
    else:
        return area
    

#5
def e_palindromo(s):
    '''
    str => str
    Verifica se a string é um palíndromo
    '''
    if s == s[::-1]:
        return "É palíndromo"
    else:
        return "Não é palíndromo"

