numbers = sorted([float (i) for i in input().split()])

first = numbers[0]

if numbers[1] == first:

    third = numbers[2]

    if numbers[3] == third:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
