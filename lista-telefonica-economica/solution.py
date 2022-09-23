while True:
    try:
        n = int(input())
        list_values = []
        for values in range(n):
            list_values.append(int(input()))
        list_values.sort()
        economy = 0
        
        for entry in range(n-1):
            number = str(list_values[entry])
            number_compare = str(list_values[entry+1])
            #verificar substrig máxima inicial
            for i in range(len(number)-1):
                if not number[:i+1] == number_compare[:i+1]:
                    economy += i
                    break
        print(economy)        
    except EOFError:
        break
    except ValueError:
        break