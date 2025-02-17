a, b, c = [int (i) for i in input().split()]

D = b**2 - 4*a*c

if D < 0:
    print("No roots")
elif D == 0:
    root_1 = -b//(2 * a)
    print(f"One root: {int(root_1)}")
else:
    root_2_1 = (-b - D**0.5)//(2 * a)
    root_2_2 = (-b + D**0.5)//(2 * a)
    print(f"Two roots: {int(min(root_2_1, root_2_2))} {int(max(root_2_1, root_2_2))}")