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
    return 'Não identificado'

def detectar_quantia(frase):
    nums = []
    for palavra in frase.split():
        if re.search(r"\d", palavra):
            nums.append(re.sub('[a-zA-Z]', '', palavra).strip(simbolos))
    return nums
def detectar_monetario(numeros, frase):
    palavra_antes = ''
    palavra_depois = ''
    texto = frase.split()
    for num in numeros:
        if num in texto:
            pass


tst = limpar('comprei 2 coxinha ontem, foi 23.50R$.')

numeros = detectar_quantia(tst)
print(tst.split())
for num in numeros:
    print(num)
    print(num in tst.split())