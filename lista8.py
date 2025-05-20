def analisa_campeonato(tabela):
    '''
    dict => tuple
    Recebe um dicionário onde as chaves são os nomes dos times
    e os valores são as suas respectivas pontuações.
    Retorna uma tupla com:
    - lista com nomes dos times
    - pontuação do campeão 
    - média de pontos por time
    '''
    # Lista com nomes dos times
    times = list(tabela.keys()) 
    # Pontuação do campeão (maior pontuação)
    pontos_campeao = max(tabela.values())    
    # Média de pontos
    media_pontos = sum(tabela.values()) / len(tabela)
    
    return (times, pontos_campeao, media_pontos)
'''
Exemplo:
    tabela = {
        'Flamengo': 70,
        'Palmeiras': 65, 
        'Botafogo': 62,
        'Bragantino': 57
    }
    print(analisa_campeonato(tabela))
'''
def converter_moeda(valor, moeda_destino):
    '''
    float, str => dict ou str
    Recebe um valor em reais e o código da moeda de destino,
    retorna um dicionário com os dados da conversão.
    Se a moeda não for reconhecida, retorna mensagem de erro.
    '''
    taxas = {
        'USD': 0.20,  
        'EUR': 0.16,  
        'GBP': 0.13  
    }
    
    moeda_destino = moeda_destino.upper()
    
    if moeda_destino not in taxas:
        return "Moeda não reconhecida"
        
    valor_convertido = valor * taxas[moeda_destino]
    
    resultado = {
        'valor_original': valor,
        'moeda_origem': 'BRL',
        'moeda_destino': moeda_destino,
        'valor_convertido': valor_convertido
    }
    
    return resultado
def conta_letra(frase, letra):
    '''
    str, str => int
    Recebe uma frase e uma letra como parâmetros e retorna
    a quantidade de vezes que a letra aparece na frase (case-sensitive)
    '''
    return frase.count(letra)

def conta_letra2(frase, letra, case):
    '''
    str, str, str => int
    Recebe uma frase, uma letra e um caractere de sensibilidade ('s' para case-sensitive
    ou 'i' para case-insensitive) e retorna a quantidade de vezes que a letra aparece na frase
    '''
    if case == 'i':
        return frase.lower().count(letra.lower())
    return frase.count(letra)

def ocorrencias_letra(frase, letra):
    '''
    str, str => tuple
    Recebe uma frase e uma letra e retorna uma tupla com os índices da primeira
    e segunda ocorrência da letra na frase (case-insensitive).
    Retorna -1 para ocorrências não encontradas.
    '''
    frase = frase.lower()
    letra = letra.lower()
    
    primeira = frase.find(letra)
    
    if primeira == -1:
        return (-1, -1)
        
    segunda = frase.find(letra, primeira + 1)
    
    if segunda == -1:
        return (primeira, -1)
        
    return (primeira, segunda)

def adiciona_a_lista(lista_inicial, *novos_itens):
    '''
    list, str => list
    Recebe uma lista inicial de compras e uma quantidade variável de strings como
    novos itens, adiciona os novos itens à lista e retorna a lista
    '''
    lista_inicial.extend(novos_itens)
    return lista_inicial


