def rails(n):
    permut = list(map(int,input().split(" ")))
    if len(permut)<n:
        return None
    b_station = []
    station = []
    mirror = [i+1 for i in range(n)]
    # mirror.reverse()
    # mudar a ordem para trabalhar com a estrutura de fila
    permut.reverse() 
    for i in range(n):
        #verificar se o vagão esperado está em permut[i]
        if permut[i]==(n-len(b_station)):
            b_station.append(permut[i])
        else:
            while (station and station[-1]==(n-len(b_station))):
                b_station.append(station.pop(-1))
            station.append(permut[i])
            
    
    while station:
       b_station.append(station.pop(len(station)-1))
    
    b_station.reverse()
    if b_station == mirror:
        return 'Yes'
    else:
        return 'No'      
    
    
    
while n:=int(input()):
    while result:=rails(n):
        print(result)
    print()