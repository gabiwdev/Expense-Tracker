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

moeda = {
    'BRL': ['reais', 'real', 'r$', ]
}

def detectar_moeda(frase):
    numeros = ''
    texto = frase.split()
    for palavra in texto:
        if re.search(r'\d', palavra):
            numeros += f'{palavra} '

    quantia = ''.join(
        caractere for caractere in numeros if caractere.isdigit()
    )

    moeda = ''.join(
        caractere for caractere in numeros if not caractere.isdigit()
    )

tst = limpar('comprei duas coxinha ontem, foi 23R$.')

detectar_moeda(tst)