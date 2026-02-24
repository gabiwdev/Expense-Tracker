## Expense-Tracker ##

Este projeto é um sistema simples em Python que permite registrar compras a partir de frases em linguagem natural, detectando automaticamente valor monetário, moeda e data.
O objetivo é transformar frases como:

Comprei um livro por 50 reais ontem (Escrita no dia 20/02/2026)

em 

19/02/2026 - 50 BRL

## Como executar 

Ao baixar o arquivo "main.py" basta abrir o cmd e digitar

```bash
cd "caminho da pasta onde o arquivo está"
```

E após isso, com Python 3.12+ instalado no computador, executar

```bash
python main.py
```

## Funcionalidades 

- Normalização de texto (remoção de acentos e pontuação)
- Detecção automática de:
  - Moeda (BRL, USD, EUR)
  - Valor numérico relacionado à moeda
  - Expressões temporais
- Cálculo automático da data com base no dia atual
- Armazenamento das compras em lista
- Exibição formatada das compras registradas

## Conceitos Aplicados 

- Programação Orientada a Objetos (POO)
- Expressões Regulares
- Manipulação de Strings
- Estruturas de Dados
- Datas com datetime

## Limitações 

- Atualmente o sistema depende de frases com uma formatação específica, onde o valor monetário esteja uma palavra antes ou depois da palavra que indique isso (real, reais, r$).
- O sistema não possui persistência.
- Ainda não há uma forma fácil de adicionar mais moedas sem ser mexendo no código base.

## Futuras Implementações 

- Detecção inteligente de categorias.
- Persistência de dados.
- API para melhor utilização
