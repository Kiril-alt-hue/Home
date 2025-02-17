n, a = map(int,input().split())
if a == 1:
    print(n*(n+1)//2)
else:
    summa = 0
    for i in range(1,n+1):
        summa += i * a**i
    print(summa)
