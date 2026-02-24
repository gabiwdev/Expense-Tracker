import unicodedata as ucd
import re
import datetime as dt

class Compra():
    def __init__(self, valor, moeda, data):
        self.valor = valor
        self.moeda = moeda
        self.data = data

    def __repr__(self):
        return f"{self.data} - {self.valor} {self.moeda}"

    def para_dicionario(self):
        return {
            'valor': self.valor,
            'moeda': self.moeda,
            'data': self.data
        }

def limpar(palavra, dicionario):
    """
    Função que normaliza a frase recebida, tirando pontuações, acentos.
    Também prepara a frase para a detecção de moeda.

    :param palavra: Frase ou palavra recebida para a normalização
    :return: Frase ou palavra já normalizada
    """

    simbolos = []

    for lista in dicionario.values():
        for item in lista:
            if not item.isalpha():
                simbolos.append(re.escape(item))


    pontuacao = ',<>´`".%&*()'

    palavra = ''.join(
        c for c in ucd.normalize('NFD', palavra)
        if ucd.category(c) != 'Mn'
    )

    palavra = palavra.lower()
    texto = palavra.split()
    texto = [t.strip(pontuacao) for t in texto]
    texto = ' '.join(texto)
    texto = re.sub(rf'(\d)({"|".join(simbolos)})', r'\1 \2', texto)
    texto = re.sub(rf'({"|".join(simbolos)})(\d)', r'\1 \2', texto)
    return texto

def detectar_moeda(frase, dicionario):
    """
    Função que detecta o tipo de moeda usado como BRL, USD ou EUR.
    Usa um dicionario com as moedas predefinidas para detectá-la.

    :param frase: Frase onde a moeda será procurada
    :param dicionario: Dicionário com as moedas e os termos identificadores delas.
    :return: Retorna o Código de Moeda ISO da moeda (ex.: BRL) ou None se não detectar
    """
    texto = frase.split()
    for chave, lista in dicionario.items():
        for item in sorted(lista, key=len, reverse=True):
            if item in texto:
                return chave
    return None

def detectar_monetario(frase, dicionario):
    """
    Detecta o valor que representa o valor monetário da frase.
    O valor considerado monetário será escolhido com base nos termos ao redor.

    :param frase: Frase a ser analisada
    :param dicionario: Dicionario com as moedas e simbolos das moedas.
    :return: Retorna o valor que a função detectar como monetário ou None caso não encontre.
    """

    tokens = frase.split()
    moeda = detectar_moeda(frase, dicionario)
    if not moeda:
        return None
    for i, palavra in enumerate(tokens):
        if palavra in dicionario[moeda]:
            anterior = tokens[i-1] if i > 0 else None
            depois = tokens[i+1] if i < len(tokens)-1 else None
            if anterior and re.search(r"\d", anterior):
                return anterior
            elif depois and re.search(r"\d", depois):
                return depois
    return None

def detectar_tempo(frase, dicionario):
    """
    Detecta a expressão de tempo como "Ontem", "Anteontem" e etc.

    :param frase: Frase a ser analisada
    :param dicionario: Dicionario com expressões de tempo predefinidas.
    :return: Retorna a expressão do tempo (ex.: Ontem) ou None caso não seja encontrada
    """

    for tempo in sorted(dicionario.keys(), key=len, reverse=True):
        padrao = rf'\b{re.escape(tempo)}'
        if re.search(padrao, frase):
            return tempo
    return 'hoje'

def calcular_tempo(expressao, dicionario):
    """
    Faz o cálculo com base na data atual.
    Reduz o tempo da data atual com base na expressão de tempo passada.

    :param expressão: Expressão usada para referência do cálculo
    :param dicionario: Dicionário com os valores de diferença de tempo em dias.
    :return: Retorna o valor da data aproximada.
    """

    data_atual = dt.date.today()
    data_aproximada = data_atual - dicionario[expressao]
    return data_aproximada

def mostrar_compras(compra: list):
    """
    Uma função que printa no output a lista de compras formatada.
    Data aproximada, valor e moeda.

    :param compra: Lista de dicionários que inclui todas as compras
    :return: Não retorna nada.
    """

    if len(compra) < 1:
        print('-- Lista de compras vazia --')

    for index, item in enumerate(compra):
        print(f"""--- Compra {index + 1} ---
{repr(item)}
"""
)

def lista_compras_dicionario(lista):
    """
    Uma função que transforma uma lista de objetos de classe "compra" em um dicionário.

    :param lista: Lista de objetos de classe "Compra"
    :return: Retorna uma lista de dicionários com o valor de cada atributo do objeto
    """

    lista_compras = []
    for compra in lista:
        lista_compras.append(compra.para_dicionario())

    return lista_compras

def carregar_compra():
    import json

    try:
        with open('compras.json', 'r') as f:
            dados = json.load(f)
    except(FileNotFoundError, json.JSONDecoder):
        return []
    print(dados)

    compras = []

    for dado in dados:
        compras.append(Compra(dado['valor'], dado['moeda'], dado['data']))

    return compras