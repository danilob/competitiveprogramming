

while True:
    try:
        n = int(input())
        if not n:
            break
        entrances = [int(i) for i in input().split()]
        sum = 0
        pay_me = 0
        for value in entrances:
            sum += value
            if (sum%100==0):
                pay_me += 1
        print(pay_me)    
    except EOFError:
        break
    except ValueError:
        break

