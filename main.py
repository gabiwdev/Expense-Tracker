import datetime as dt
import string
import unicodedata as ucd
import re

moedas = {
    'BRL': ['r$' ,'reais', 'real'],
    'USD': ['dolar', 'dolares', '$'],
    'EUR': ['euro', 'euros', '€']
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
    return texto



print(simbolos)
def detectar_moeda(frase, dict):
    for chave, lista in dict.items():
        for item in sorted(lista, key=len, reverse=True):
            if item in frase:
                return chave
    return 'Não identificado'

def detectar_quantia(frase):
    nums = []
    for palavra in frase.split():
        if re.search(r"\d", palavra):
            nums.append(re.sub('[a-zA-Z]', '', palavra).strip(''.join(simbolos)))
    return nums
def detectar_monetario(numeros, frase, dict):
    palavra_antes = ''
    palavra_depois = ''
    texto = frase.split()
    for chave, lista in dict.items():
        for item in lista:
            if not item.isalpha():
                continue
            if item in texto:
                palavra_antes = texto[(texto.index(item) - 1)]
                palavra_depois = texto[(texto.index(item) + 1)]

            if palavra_antes.isdigit():
                return palavra_antes
            if palavra_depois.isdigit():
                return palavra_depois

tst = limpar('comprei 2 coxinha ontem, foi 23.50R$.')
print(tst)
