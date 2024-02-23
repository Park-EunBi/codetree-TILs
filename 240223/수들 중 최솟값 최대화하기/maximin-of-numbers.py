n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
ans = -float('inf')

def find_min():
    minimum = float('inf')
    for idx, c in enumerate(choice):
        minimum = min(minimum, board[idx][c])
    return minimum

choice = []
def choose(num):
    global ans
    if num == n:
        ans = max(ans, find_min())
        return 

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            choice.append(i)
            choose(num + 1)
            visited[i] = 0
            choice.pop()


choose(0)
print(ans)