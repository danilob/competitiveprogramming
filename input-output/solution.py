

while True:
    try:
        n = int(input())
        print(n)
        for i in range(n):
            #mesmo tipo
            #height, weight = [int(i) for i in input().split()]
            data = input().split()
            height = float(data[0])
            weight = int(data[1])
            print(f'Height: {height}; Weight: {weight}')
    except EOFError:
        break
    except ValueError:
        break