#Aula 1 - Conceitos Básicos
#Questão 1
def celsius_para_fahrenheit(n):
    '''
    float => float
    '''
    fahrenheit = (n*1.8)+32
    return fahrenheit

#Questão 2
def horario_despertador(n1,n2):
    '''
    int => int
    '''
    return (n1+n2)%24

#Questão 3
def torricelli(altura):
    '''
    float => float
    '''
    velocidade = (2*9.81*altura)**0.5
    return velocidade 
#Questão 4
def sistema_linear_2d(a,b,c,d,y1,y2):
    '''
    float,float,float,float,float,float => float,float
    '''
    detCoef = a*d - b*c
    matAx = d*y1 - b*y2
    matAy = a*y2 - c*y1
    x1 = matAx / detCoef
    x2 = matAy / detCoef
    return f"{x1},{x2}"

#Questão 5
def horario_chegada(horasAt, minAt, minDur):
    '''
    int,int,int => int,int
    '''
    minTotal = (minAt + minDur)%60
    hTotal = horasAt + (minAt+minDur)//60
    return f"{hTotal},{minTotal}"

#Questão 6
def corrente(fonte,r1,r2,r3):
    '''
    float,float,float,float => float
    '''
    return fonte/((1/r2+1/r3)**-1+r1)

    

    
