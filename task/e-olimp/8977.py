s = input()

first = s[2] + s[6] + s[10] # перший пункт

second = s[0] + s[-2] + s[-1] # другий пункт

third = s[:7] # третій пункт

fourth = s[4:] # четвертий пункт

fifth = "" # п'ятий пункт
for i in range(len(s)):
    if i % 2 != 0:
        fifth += s[i]

sixth = len(fifth) # шостий пункт

seventh = s[::-1] # сьомий пункт
        

print(f"{first}\n{second}\n{third}\n{fourth}\n{fifth}\n{sixth}\n{seventh}")