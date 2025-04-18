def degree_of_symmetry(N):
    s = str(N)
    length = len(s)
    count = 0

    for i in range((length + 1) // 2):
        if s[i] == s[length - 1 - i]:
            count += 1

    return count

N = input()
print(degree_of_symmetry(N))