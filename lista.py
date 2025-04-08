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
    somaHora = n1+n2
    while somaHora>=24:
        somaHora -= 24
    return somaHora

#Questão 3
#Questão 4
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

    

    