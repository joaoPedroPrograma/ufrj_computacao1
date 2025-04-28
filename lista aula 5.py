#1
def sinal_numero(n):
    '''
    float => str
    '''
    if n > 0:
        return "Positivo."
    elif n < 0:
        return "Negativo."
    else:
        return "Zero."
    
#2
def nota(n):
    '''
    float => str 
    '''
    if 9 <= n <=10:
        return "A"
    elif 8<=n <9:
        return "B"
    elif 7<=n<8:
        return "C"
    elif 0<=n<7:
        return "D"
    else:
        return "Nota fora do intervalo"

#3
def classificar_triangulo(l1,l2,l3):
    '''
    float,float,float => str
    '''
    equilatero = (l1==l2==l3)
    isosceles = ((l1==l2) and (l2!=l3)) or ((l2==l3) and (l2!=l1)) or ((l1==l3) and (l3!=l2))
    escaleno = l1!=l2 and l1!=l3 and l2!=l3
    erroTriangulo = ((l1+l2)<=l3) or ((l2+l3)<=l1) or((l1+l3)<=l2)
    if erroTriangulo:
        return "Os valores fornecidos não formam um triangulo válido"
    elif equilatero:
        return "Triângulo equilátero"
    elif isosceles:
        return "Triângulo isósceles"
    elif escaleno:
        return "Triângulo escaleno"
    


#4
def bissextualidade(ano):
    '''
    int => str
    '''
    verificador = ano %4 == 0 and (ano % 100!= 0 or ano %400 == 0)
    if verificador:
        return f"O Ano {ano} é bissexto"
    else:
        return f"O Ano {ano} não é bissexto"

#5
def dias(dia_inicial,duracao_estadia):
    '''
    int,int->str
    '''
    if ((dia_inicial + duracao_estadia)%7)==0:
        return "Domingo"
    elif ((dia_inicial + duracao_estadia)%7)==1:
        return "Segunda"
    elif ((dia_inicial + duracao_estadia)%7)==2:
        return "Terça"
    elif ((dia_inicial + duracao_estadia)%7)==3:
        return "Quarta"
    elif ((dia_inicial + duracao_estadia)%7)==4:
        return "Quinta"
    elif ((dia_inicial +duracao_estadia)%7)==5:
        return "Sexta"
    else:
        return "Sábado"
#6
def salario_diario(valor, horas, dia):
    '''
    float, int, str => float
    '''
    if (dia == 'segunda-feira' or dia=='terça-feira' or dia=='quarta-feira' 
        or dia=='quinta-feira' or dia=='sexta-feira' or dia=='sábado'):
        grana = valor * horas
        return grana
    elif dia == 'domingo':
        grana = 2*(valor*horas)
        return grana
    else:
        return 'Insira termos válidos, exemplo: (10,8,"segunda-feira")'

#7
import math as m
def raizes_eq_quadratica(a,b,c):
    '''
    Caso delta > 0
    float, float, float => float, float
    delta == 0
    float, float, float => float
    '''
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b + m.sqrt(delta))/(2*a)
        x2 = (-b - m.sqrt(delta))/(2*a)
        return x1,x2
    elif delta == 0:
        x1 = -b/2*a
        return x1
    else:
        return "A equacao nao possui raizes reais"
    
#8
def valor_final_produto(preço,categoria):
    '''
    float, str => float
    '''
    if categoria == 'eletrônico':
        preço = preço *0.9
    elif categoria == 'vestuário':
        preço = preço * 0.95
    elif categoria == 'alimento':
        preço = preço
    else:
        return 'Insira uma entrada válida, exemplo: (500, "eletrônico")'
    if preço > 1000:
        preço = preço * 1.15  
    elif 500 <=preço<=1000:
        preço = preço * 1.10  
    elif preço < 500:
        preço = preço * 1.05  
    return round(preço, 2)

#9
def deduçãoIR(n):
    '''
    float => str
    ou
    float => float
    '''
    if n <= 1903.98:
        return "Isento"
    elif 1903.98 <= n <= 2826.65:
        return n*0.075
    elif 2826.65 <= n <= 3751.05:
        return n*0.15
    elif 3751.05 <=n<=4664.68:
        return n*0.225
    else:
        return n*0.275

#10
def quantidade_raizes(a,b,c):
    '''
    float, float, float => str
    '''
    delta = b**2-4*a*c
    if delta < 0:
        return "Nenhuma raiz real"
    elif delta ==0:
        return "Uma raiz real"
    else:
        return "Duas raízes reais"


