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


def detectar_moeda(frase):
    números = []
    texto = frase.split()
    for palavra in texto:
        if re.search(r'\d', palavra):
            números.append(palavra)
    print(números)

tst = limpar('comprei duas coxinha ontem, foi 23R$.')

detectar_moeda(tst)