import datetime as dt
import string
import unicodedata as ucd
import re

moedas = {
    'BRL': ['r$' ,'reais', 'real'],
    'USD': ['dolar', 'dolares', '$'],
    'EUR': ['euro', 'euros', '€']
}

tempo_indicador = {
    'ontem': dt.timedelta(days=1),
    'anteontem': dt.timedelta(days=2),
    'hoje': dt.timedelta(days=0),
    'semana passada': dt.timedelta(days=7),
    'mês passado': dt.timedelta(days=30),
    'mês atrás': dt.timedelta(days=30),
    'semana atrás': dt.timedelta(days=30)
}

simbolos = []

for lista in moedas.values():
    for item in lista:
        if not item.isalpha():
            simbolos.append(re.escape(item))

print(f'{"|".join(simbolos)}')

def limpar(palavra):

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

print(simbolos)
def detectar_moeda(frase, dict):
    texto = frase.split()
    for chave, lista in dict.items():
        for item in sorted(lista, key=len, reverse=True):
            if item in texto:
                return chave
    return None

def detectar_monetario(frase, dict):
    tokens = frase.split()
    moeda = detectar_moeda(frase, dict)
    if not moeda:
        return None
    for i, palavra in enumerate(tokens):
        if palavra in dict[moeda]:
            anterior = tokens[i-1] if i > 0 else None
            depois = tokens[i+1] if i < len(tokens)-1 else None
            if anterior and re.search(r"\d", anterior):
                return anterior
            elif depois and re.search(r"\d", depois):
                return depois
    return None

def detectar_tempo(frase):
    for tempo in sorted(tempo_indicador.keys(), key=len, reverse=True):
        padrão = rf'\b{re.escape(expressão)}'
        if re.search(padrão, frase):
            return expressão
    return None

tst = limpar('comprei 2 coxinha ontem, foi 23.50R$.')
print(detectar_monetario(tst, moedas))

time = dt.date.today()
timet = dt.timedelta(days=50)
print(time - timet)