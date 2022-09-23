while True:
    try:
        n = int(input())
        if n<0:
            break
        sum = int(n*(n+1)*(2*n+1)/6)
        print(sum)
    except EOFError:
        break
    except ValueError:
        break