from collections import deque
import math

while True:
    try:
        n_palavras, l_por_pagina, c_por_linha = list(map(int,input().split()))
        text = input().split()
        structure_text = deque(text)
        # print(structure_text)
        lines = 1
        sum_character = 0
        while structure_text:
            word = structure_text.popleft()
            sum_character += len(word)
            if sum_character > c_por_linha:
                # print('nova linha')
                structure_text.appendleft(word)
                sum_character = 0
                lines += 1
            else:
                # print('pop', word)
                sum_character += 1 #espaço
        # print('linhas',lines)
        print(math.ceil(lines/l_por_pagina))        
    except EOFError:
        break
    except ValueError:
        break