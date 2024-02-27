n, t = map(int, input().split())
board = list(map(int, input().split())) + (list(map(int, input().split())))

for _ in range(t):
    temp = board[-1]
    for i in range(2 * n - 1, 0, -1):
        board[i] = board[i - 1]
    board[0] = temp

print(*board[:n])
print(*board[n:])