x, a, y = input().split()

if a == '+':
    print(x, a, y, '=', int(x) + int(y))
elif a == '-':
    print(x, a, y, '=', int(x) - int(y))
elif a == '*':
    print(x, a, y, '=', int(x) * int(y))
elif a == '/':
    print(x, a, y, '=', int(x) // int(y))