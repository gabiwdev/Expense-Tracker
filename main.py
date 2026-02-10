import datetime as dt
import string
import unicodedata as ucd



def limpar(palavra):
    palavra = ''.join(
        c for c in ucd.normalize('NFD', palavra)
        if ucd.category(c) != 'Mn'
    )

    palavra = palavra.lower()
    texto = palavra.split()
    texto = [t.strip(string.punctuation) for t in texto]

    return ' '.join(texto)


