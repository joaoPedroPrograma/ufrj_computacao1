#1
def elegibilidade(idade):
    '''
    int => bool
    '''
    verificador = idade >=18
    return f"A pessoa é elegível para votar? {verificador}"

#2
def bissextualidade(ano):
    '''
    int => bool
    '''
    verificador = ano %4 == 0 and (ano % 100!= 0 or ano %400 == 0)
    return f"O ano é bissexto? {verificador}"

#3
def pontoCirculo(x,y,r):
    '''
    float, float, float => bool
    '''
    return x**2 + y**2 <= r**2
#4
def coracaoDeMae(friends, carros):
    '''
    int, int => bool
    '''
    assentos = 5 * carros
    verificador = friends <=assentos
    return verificador
#5
#6
def botaCasacoTiraCasaco(temp):
    '''
    float => str
    '''
    return ((temp < 10) * 'Muito frio' + (10 <= temp <= 17) * 'Frio' +
        (18 <= temp <= 25) * 'Agradável' + (26 <= temp <= 35) * 'Quente' +
        (temp > 35) * 'Muito quente')
    

#7
