#1
def elegibilidade(idade):
    verificador = idade >=18
    return f"A pessoa é elegível para votar? {verificador}"

#2
def bissextualidade(ano):
    verificador = ano %4 == 0 and (ano % 100!= 0 or ano %400 == 0)
    return f"O ano é bissexto? {verificador}"

#3
def pontoCirculo(x,y,r):
    return x**2 + y**2 <= r**2
#4
def coracaoDeMae(friends, carros):
    assentos = 5 * carros
    verificador = friends <=assentos
    return verificador
#5
#6
def botaCasacoTiraCasaco(temp):
    if temp < 10:
        return "Muito frio"
    elif 10 >= temp <=17:
        return "Frio"
    elif 18 >= temp <=25:
        return "Agradável"
    elif 26 >= temp <= 35:
        return "Quente"
    else:
        return "Muito quente" 
    
