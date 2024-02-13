n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(node):
    global cnt
    visited[node] = 1
    for n in graph[node]:
        if not visited[n]:
            # visited[n] = 1
            cnt += 1
            dfs(n)

dfs(1)
print(cnt)