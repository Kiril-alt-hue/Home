n = int(input())
t = input()
digits = [int(x) for x in t.split()]

last = str(digits[-1])
num = [int(x) for x in last.split()]

del digits[-1]

result = num + digits
print(*result)