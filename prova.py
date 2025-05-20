def baskara(coef):
    a, b, c = coef
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return ['Complexo', 'Complexo', 'Complexo']
    
    x1 = (-b + (delta)**0.5)/(2*a)
    x2 = (-b - (delta)**0.5)/(2*a)
    
    media = (x1 + x2)/2
    
    eixo1 = 'Eixo x positivo' if x1 > 0 else ('Eixo x negativo' if x1 < 0 else 'Origem')
    eixo2 = 'Eixo x positivo' if x2 > 0 else ('Eixo x negativo' if x2 < 0 else 'Origem')
            
    return [(x1, x2), media, (eixo1, eixo2)]



def ajustarTemp(tanque, variacao_temp):
    tanque['tempAtual'] += variacao_temp
    tanque['ajustesRealizados'] += 1
    if tanque['maiorVariacao'] < abs(variacao_temp):
        tanque['maiorVariacao'] = abs(variacao_temp)
    return tanque

def calMedia(infoAlunos):
    # Expandir as listas para acomodar situação e média
    infoAlunos['aluno1'].extend(['', 0])
    infoAlunos['aluno2'].extend(['', 0])
    
    mediaAluno1 = (infoAlunos['aluno1'][0] + infoAlunos['aluno1'][1])/2
    mediaAluno2 = (infoAlunos['aluno2'][0] + infoAlunos['aluno2'][1])/2
    
    infoAlunos['aluno1'][4] = mediaAluno1
    infoAlunos['aluno2'][4] = mediaAluno2
    
    if mediaAluno1 <5 or infoAlunos['aluno1'][2] > 25:
        infoAlunos['aluno1'][3] = 'Reprovado'
    elif (5<=mediaAluno1 <7 and infoAlunos['aluno1'][2] <= 25):
        infoAlunos['aluno1'][3] = 'Prova Final'
    elif (7<=mediaAluno1 <=10 and infoAlunos['aluno1'][2] <= 25):
        infoAlunos['aluno1'][3] = 'Aprovado'
        
    if mediaAluno2 <5 or infoAlunos['aluno2'][2] > 25:
        infoAlunos['aluno2'][3] = 'Reprovado'
    elif (5<=mediaAluno2 <7 and infoAlunos['aluno2'][2] <= 25):
        infoAlunos['aluno2'][3] = 'Prova Final'
    elif (7<=mediaAluno2 <=10 and infoAlunos['aluno2'][2] <= 25):
        infoAlunos['aluno2'][3] = 'Aprovado'
        
    return infoAlunos

    '''
    Pontos principais dos conteúdos abordados:
    
    1. Operadores matemáticos e lógicos:
    - Operações básicas: soma (+), subtração (-), multiplicação (*), divisão (/)
    - Potenciação (**) - usado para calcular raiz quadrada com **0.5
    - Operadores de comparação: menor (<), maior (>), menor igual (<=), maior igual (>=), igual (==)
    - Operadores lógicos: and (ambas condições verdadeiras), or (uma ou outra verdadeira)
    - Função abs() para calcular valor absoluto de um número
    
    2. Estruturas condicionais:
    - if/elif/else para controle de fluxo
    - Operador ternário: forma resumida de if/else em uma linha
      Exemplo: resultado = 'pos' if x > 0 else 'neg'
    - Condições aninhadas e múltiplas condições com and/or
    
    3. Estruturas de dados e seus métodos:
    - Listas:
      * extend() - adiciona elementos de outra lista
      * indexação com [] para acessar elementos
      * Operações com elementos (soma, média)
    - Dicionários:
      * Acesso por chaves com ['chave']
      * Atualização de valores
      * Aninhamento de estruturas (dicionários com listas)
    - Tuplas:
      * Retorno múltiplo de valores
      * Empacotamento/desempacotamento
    
    4. Funções:
    - Definição com def e parâmetros
    - Docstrings com descrição, parâmetros e retorno
    - Retorno de diferentes tipos (listas, dicionários, tuplas)
    - Processamento de dados e cálculos
    
    5. Manipulação de dados:
    - Cálculo de médias
    - Verificação de condições
    - Atualização de estruturas de dados
    - Transformação de dados
    
    6. Boas práticas:
    - Nomes descritivos (camelCase para funções)
    - Indentação consistente
    - Documentação clara
    - Organização lógica do código
  
    Distinção entre Tuplas e Listas:
    
    1. Tuplas:
    - Imutáveis (não podem ser alteradas após criação)
    - Definidas com parênteses () ou sem delimitadores
    - Mais eficientes em memória
    - Ideais para dados que não mudam
    - Exemplo: coordenadas = (10, 20)
    
    2. Listas:
    - Mutáveis (podem ser modificadas)
    - Definidas com colchetes []
    - Mais flexíveis para alterações
    - Ideais para coleções que mudam
    - Exemplo: notas = [7.5, 8.0, 9.0]
    
    Uso dos dois pontos em listas:
    
    1. Fatiamento (slicing):
    - lista[início:fim] - elementos do índice início até fim-1
    - lista[:fim] - do início até fim-1
    - lista[início:] - do início até o final
    - lista[::passo] - define intervalo entre elementos
    
    2. Representações:
    - lista[1:4] - elementos dos índices 1, 2 e 3
    - lista[-3:] - últimos 3 elementos
    - lista[::-1] - inverte a lista
    - lista[::2] - elementos em posições pares
    
    3. Passos:
    - Valor positivo: avança na lista (ex: lista[::2] pega elementos alternados)
    - Valor negativo: percorre a lista de trás pra frente (ex: lista[::-1] inverte)
    - Quanto maior o valor absoluto, maior o intervalo entre elementos
    - Exemplos:
      * lista[::3] - pega todo terceiro elemento
      * lista[::4] - pega todo quarto elemento
      * lista[::-2] - pega elementos alternados de trás pra frente
    '''
    '''
    Tipos de Dados em Python:
    
    1. Tipos Primitivos:
    
    Números:
    - int: números inteiros (ex: 42, -17, 0)
    - float: números decimais (ex: 3.14, -0.001, 2.0)
    - complex: números complexos (ex: 3+4j)
    
    Texto:
    - str: cadeia de caracteres (ex: "Python", 'Olá')
    
    Booleano:
    - bool: valores lógicos True ou False
    
    Nulo:
    - NoneType: valor especial None que representa "nada" ou "nulo"
    
    Características dos primitivos:
    - São imutáveis
    - Servem como blocos básicos
    - Possuem operações específicas
    - São implementados nativamente
    
    2. Tipos Não-Primitivos (Estruturas de Dados):
    
    Sequências:
    - list: lista mutável de elementos [1, 2, 3]
    - tuple: sequência imutável de elementos (1, 2, 3)
    
    Coleções:
    - set: conjunto não ordenado de elementos únicos {1, 2, 3}
    - dict: mapeamento de chaves para valores {'a': 1, 'b': 2}
    
    Características dos não-primitivos:
    - Podem ser mutáveis ou imutáveis
    - Armazenam coleções de outros tipos
    - Permitem operações mais complexas
    - São construídos a partir dos tipos primitivos
    '''


