from cgitb import text


while True:
    try:
        text1 = input()
        text2 = input()
        #verificar substrig máxima
        max_size = 0
        for i in range(len(text1)):
            max_size_before = max_size
            # print('for i',i)
            for j in range(len(text1)-i):
                # print('compare', text1[j:j+i+1], 'em', text2)
                if text1[j:j+i+1] in text2:
                    max_size += 1
                    break
            if max_size_before == max_size:
                break
        print(max_size)        
    except EOFError:
        break
    except ValueError:
        break