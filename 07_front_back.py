"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    L = []
    for l in a, b:
        l1, l2 = l[:len(l) // 2 + len(l) % 2], l[len(l) // 2 + len(l) % 2:]
        L.extend([l1, l2])
    return ''.join([L[0], L[2], L[1], L[3]])

    # a1, a2 = a[:len(a) // 2 + len(a) % 2], a[len(a) // 2 + len(a) % 2:]
    # b1, b2 = b[:len(b) // 2 + len(b) % 2], b[len(b) // 2 + len(b) % 2:]
    # return ''.join([a1, b1, a2, b2])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
