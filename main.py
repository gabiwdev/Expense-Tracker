import datetime as dt
import string
import unicodedata as ucd
import re



def limpar(palavra):

    pontuacao = ',<>´`".%&*()'

    palavra = ''.join(
        c for c in ucd.normalize('NFD', palavra)
        if ucd.category(c) != 'Mn'
    )

    palavra = palavra.lower()
    texto = palavra.split()
    texto = [t.strip(pontuacao) for t in texto]

    return ' '.join(texto)

moedas = {
    'BRL': ['reais', 'real', 'r$'],
    'USD': ['dolar', 'dolares', '$'],
    'EUR': ['euro', 'euros', '€']
}

simbolos = '$€'

def detectar_moeda(frase, dict):
    for chave, lista in dict.items():
        for item in sorted(lista, key=len, reverse=True):
            if item in frase:
                return chave

def detectar_quantia(frase):
    nums = []
    for palavra in frase.split():
        if re.search(r"\d", palavra):
            nums.append(re.sub('[a-zA-Z]', '', palavra).strip(simbolos))




tst = limpar('comprei duas coxinha ontem, foi 23.50.')

print(tst.split())
print(re.search(r"\d", tst))

detectar_quantia(tst)