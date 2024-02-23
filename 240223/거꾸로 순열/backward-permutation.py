n = int(input())

visited = [0 for _ in range(n + 1)]

choice = []
def choose(num):
    if num == n:
        print(*choice)
        return 
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = 1
            choice.append(i)
            choose(num + 1)
            visited[i] = 0
            choice.pop()

choose(0)