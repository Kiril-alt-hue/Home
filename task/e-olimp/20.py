n = int(input())

count = 0

while n > 0:
    new_n = n - sum(int(i) for i in str(n))
    n = new_n
    count += 1

print(count)