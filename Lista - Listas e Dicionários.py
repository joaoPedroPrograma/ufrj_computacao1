#1
def substitui_elemento(indice, novo_valor):
    '''
    int, int => list
    '''
    lista = [1, 2, 3, 4, 5]
    lista[indice] = novo_valor
    return lista
#2
def produto_escalar(lista1, lista2):
    '''
    list, list => int
    Recebe duas listas com 2 elementos cada e retorna
    a soma dos produtos dos elementos correspondentes
    '''
    return lista1[0] * lista2[0] + lista1[1] * lista2[1]
#3
def velocidade_media(distancias, tempos):
    '''
    list, list => float ou str
    Recebe duas listas com 3 elementos cada, uma contendo distâncias em km
    e outra contendo tempos em minutos, e retorna a velocidade média em km/h.
    Se as listas não tiverem exatamente 3 elementos, retorna mensagem de erro.
    '''
    if len(distancias) != 3 or len(tempos) != 3:
        return "Ao menos uma lista não possui 3 elementos"
        
    distancia_total = sum(distancias)
    tempo_total = sum(tempos)
    
    tempo_horas = tempo_total / 60
    
    velocidade = distancia_total / tempo_horas
    
    return round(velocidade, 1)
#4
def dados_alunos(nome, nota1, nota2):
    '''
    str, float, float => dict
    Recebe o nome do aluno e duas notas, cria um dicionário com esses dados
    e adiciona a média das notas, retornando o dicionário completo
    '''
    dicionario = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2
    }
    
    dicionario['média'] = (nota1 + nota2) / 2
    
    return dicionario
#5
def situacao_aluno(dados):
    '''
    dict => dict
    Recebe um dicionário com nome e notas do aluno e retorna o mesmo dicionário
    acrescido da situação (aprovado/reprovado) baseada na média das notas
    '''
    media = (dados['nota1'] + dados['nota2']) / 2
    
    if media >= 7.0:
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'
        
    return dados
#6
def converter_moeda(valor, moeda_destino):
    '''
    float, str => dict ou str
    Recebe um valor em reais e o código da moeda de destino,
    retorna um dicionário com os dados da conversão.
    Se a moeda não for reconhecida, retorna mensagem de erro.
    '''
    taxas = {
        'USD': 0.18,  
        'EUR': 0.16,  
        'GBP': 0.13  
    }
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

''''


              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||


     hit any key to continue
'''
















