def multiplica_matriz_por_numero(numero, matriz):
    """
    int, list > list
    """
    nova_matriz = []
    for linha in matriz:
        nova_linha = [numero * elemento for elemento in linha]
        nova_matriz.append(nova_linha)
    return nova_matriz

def deu_match(afinidades):
    """
    dict > list
    """
    resultado = []
    for pessoa, lista in afinidades.items():
        for outra in lista:
            if outra in afinidades and pessoa in afinidades[outra]:
                par = tuple(sorted([pessoa, outra]))
                if par not in resultado:
                    resultado.append(par)
    return resultado

def quem_ligou(numero, agenda):
    """
    str, list > list
    """
    for contato in agenda:
        if contato[2] == numero:
            return contato
    return []

def contar_letra_b(lista):
    """
    list > int
    """
    contador = 0
    for palavra in lista:
        contador += palavra.lower().count('b')
    return contador

def contar_letra(lista, letra):
    """
    list, str > int
    """
    contador = 0
    for palavra in lista:
        contador += palavra.lower().count(letra.lower())
    return contador

def eh_matriz_identidade(matriz):
    """
    list > bool
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True

def transpor_matriz(matriz):
    """
    list > list
    """
    transposta = []
    for j in range(len(matriz[0])):
        nova_linha = []
        for i in range(len(matriz)):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)
    return transposta

def soma_matrizes(matriz_a, matriz_b):
    """
    list, list > list or None
    """
    if len(matriz_a) != len(matriz_b):
        return None
    for i in range(len(matriz_a)):
        if len(matriz_a[i]) != len(matriz_b[i]):
            return None

    resultado = []
    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_a[i])):
            linha.append(matriz_a[i][j] + matriz_b[i][j])
        resultado.append(linha)
    return resultado


