#1
def faixaEtaria(idade):
    '''
    int => str
    '''
    bebe = 0>idade<=3
    crianca = 3<idade<=10
    adolescente = 10<idade<=18
    adulta= 18<idade<=60
    idosa = idade > 60
    return ("Bebê"*bebe or "Criança"*crianca or 
            "Adolescente"*adolescente or "Adulta"*adulta or "Idosa"*idosa)

#2
def situacaoAcademica(prova1,prova2,trabalho, faltas):
    '''
    float, float, float, int => str
    '''
    media = (prova1*3+prova2*5+trabalho*2)/10 
    repFalta = faltas >=15
    rep = media < 3
    provaFinal = 3<media<7
    aprovado = media >=7
    return ("Reprovado por falta"*repFalta or "Reprovado"*rep or 
            "Fará Prova Final"*provaFinal or "Aprovado"*aprovado)
    
#3
def qualQuadrante(x,y):
    '''
    float, float => str
    '''
    quad1 = x > 0 and y > 0
    quad2 = x < 0 and y > 0
    quad3 = x < 0 and y < 0
    quad4 = x > 0 and y < 0
    null = x==0 or y==0
    return ("Primeiro"*quad1 or "Segundo"*quad2 or "Terceiro"*quad3 or "Quarto"*quad4 or 
            "Pelo menos uma das coordenadas é 0. O ponto não pertence a nenhum dos quadrantes"
            *null)

#4 => https://github.com/joaoPedroPrograma/ufrj/blob/main/exerc%C3%ADcio4.pdf
#5
def emprestimo(idade, patrimonio, valorEmprestado, parcelas):
    '''
    int, float, float, int => int, float
    '''
    fatorIdade = ((18<= idade <=30) *3 + (31<=idade<=50) *6 + 
              (51<=idade<=60) *9 + (idade >60)*12)
    fatorPat = ((0<=patrimonio<=50000) *2 + (50000<patrimonio<=200000) *1 +
            (200000<patrimonio<=1000000) *-1 + (patrimonio > 1000000) *-2)
    fatorDeRisco = fatorIdade + fatorPat
    jurosAnuais = 1.8 + fatorDeRisco *0.2
    jurosMensais = jurosAnuais / 12
    mensalidade = (valorEmprestado * (1 + jurosMensais) ** parcelas) / parcelas
    return f"{fatorDeRisco}, {mensalidade}"