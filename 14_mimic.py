"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict


def open_file(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', ' ')
        words = data.lower().split()
    return words


def mimic_dict(filename):
    """
    Return the mimic dict mapping each word for the list of subsequent words.
    """
    words = open_file(filename)
    dct = defaultdict(list)
    dct[''] = [words[0]]
    for i, word in enumerate(words[:-1]):
        adjc = words[i + 1]
        dct[word].append(adjc)
    dct[words[-1]] = ['']
    return dct


def print_mimic(mimic_dict, word):
    """
    Print a text with 200 words from the mimic dict and the initial word.
    """
    initial = word
    dct = mimic_dict
    phrase = []
    while len(phrase) <= 200:
        phrase.append(initial)
        initial = random.choice(dct[phrase[-1]])
    return ' '.join(phrase)


# Call the mimic_dict() and print_mimic() functions
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print(print_mimic(dict, ''))


if __name__ == '__main__':
    main()
