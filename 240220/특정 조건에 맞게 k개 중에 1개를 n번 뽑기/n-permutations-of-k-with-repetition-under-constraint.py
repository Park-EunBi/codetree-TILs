k, n = map(int, input().split())

ret = []
def choice(num):
    if num == n:
        print(*ret)
        return 
    
    for i in range(1, k + 1):
        if num >= 2 and i == ret[num - 1] == ret[num - 2]:
            continue
        else:
            ret.append(i)
            choice(num + 1)
            ret.pop()

choice(0)