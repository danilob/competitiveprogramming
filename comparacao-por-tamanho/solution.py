def by_len(e):
    return len(e)

while True:
    try:
        n = int(input())
        for line in range(n):
            text = input()
            list_text = text.split()
            list_text.sort(reverse=True,key=by_len)
            print(' '.join(list_text)) 
    except EOFError:
        break
    except ValueError:
        break

