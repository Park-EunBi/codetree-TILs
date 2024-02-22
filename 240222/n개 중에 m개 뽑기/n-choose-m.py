n, m = map(int, input().split())

choice = []
def choose(num, before): # 자릿수, 이전 수 
    if num == m:
        print(*choice)
        return 
    
    for i in range(before, n + 1):
        choice.append(i)
        choose(num + 1, i + 1)
        choice.pop()

choose(0, 1)