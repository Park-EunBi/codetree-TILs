n, t = map(int, input().split())
one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))

for _ in range(t):
    temp = one[-1]
    # one 이동 
    for i in range(n - 1, 0, -1):
        one[i] = one[i - 1]
    
    # two 이동 
    temp_2 = two[-1]
    for i in range(n - 1, 0, -1):
        two[i] = two[i - 1]
    two[0] = temp

    # three 이동 
    temp = three[-1]
    for i in range(n - 1, 0, -1):
        three[i] = three[i - 1]
    three[0] = temp_2

    one[0] = temp

print(*one)
print(*two)
print(*three)