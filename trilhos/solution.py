while True:
    try:
        n = int(input())
        while True:
            permut = input()
            if len(permut)==1 and permut[0]=='0':
                print()
                break
            vagoes = list(map(int,permut.split()))
            vagoes.reverse()
            to_b = []
            station = []
            for vagao in vagoes:
                if vagao == (n-len(to_b)):
                    to_b.append(vagao)
                    while len(station):
                        vagao_station = station.pop()
                        if vagao_station == (n-len(to_b)):
                            to_b.append(vagao_station)
                        else:
                            station.append(vagao_station)
                            break
                else:
                    station.append(vagao)
            if (len(station)):
                print('No')
            else:
                print('Yes')
            # while len(station):
            #     vagao_station = station.pop()
            #     to_b.append(vagao_station)
            
    except EOFError:
        break
    except ValueError:
        break

