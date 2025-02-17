n = [int (i) for i in input().split()]

count = 0
count_par = 0

while count_par != 4:
    del n[0]
    maxim = max(n)
    count+=maxim
    count_par+= 1
    n.remove(maxim)

print(count)
