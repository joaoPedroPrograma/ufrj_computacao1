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
    

#8
def valor_final_produto(preço,categoria):
    '''
    float, str => float
    '''
    if categoria == 'eletrônico':
        preço = preço *0.9
    elif categoria == 'estuário':
        preço * 0.95
    elif categoria == 'alimento':
        preço*1
    if preço > 1000:
        preço = preço * 1.15  
    elif 500 <=preço<=1000:
        preço = preço * 1.10  
    elif preço < 500:
        preço = preço * 1.05  
    return preço


#9
def deduçãoIR(n):
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
    delta = b**2-4*a*c
    if delta < 0:
        return "Nenhuma raiz real"
    elif delta ==0:
        return "Uma raiz real"
    else:
        return "Duas raízes reais"
