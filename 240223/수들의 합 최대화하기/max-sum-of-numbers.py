n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [0 for _ in range(n)]
ans = -float('inf')

def make_sum():
    make = 0
    for idx, c in enumerate(choice):
        make += board[idx][c]
    
    return make

# 1. 색칠할 칸 선택하기 
choice = []
def choose(num):
    global ans
    if num == n:
        # 2. 합 구하고, 최댓값 갱신 
        ans = max(ans, make_sum())       
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