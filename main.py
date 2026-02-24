import funcoes as f
import datetime as dt
import json


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
    'semana atrás': dt.timedelta(days=7)
}

compras = f.carregar_compra()
continuar = True

while continuar:
    lista = input('Quer mostrar sua lista de compras? (S/N) ')
    if lista.strip().lower() in 's':
        f.mostrar_compras(compras)


    frase = f.limpar(str(input('Escreva a frase: ')), moedas)
    valor = f.detectar_monetario(frase, moedas)
    moeda = f.detectar_moeda(frase, moedas)
    tempo = f.detectar_tempo(frase, tempo_indicador)
    dia = f.calcular_tempo(tempo, tempo_indicador)
    dia_formatado = dia.strftime("%d/%m/%Y")

    compras.append(f.Compra(valor, moeda, dia_formatado))

    with open('compras.json', 'w') as json_file:
        json.dump(f.lista_compras_dicionario(compras), json_file, indent=4)

    print(compras)

    decisao = input('Quer continuar? (S/N) ')
    if decisao.strip().lower() in 's':
        continuar = True
    else:
        print(f.lista_compras_dicionario(compras))
        continuar = False