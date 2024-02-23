n = int(input())
board= [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n + 1)]

ans = float('inf')

def calc():
    total = 0
    # 1으로 되돌아 옴 (idx 처리 -> -1)
    choice.append(0)
    for j in range(len(choice) - 1):
        total += board[choice[j]][choice[j + 1]]
    choice.pop() # 넣었던 것 다시 pop (조합 재 생성 위해)
    return total

# 1에서 출발 (idx 처리 -> -1)
choice = [0]
def choose(num):
    global ans
    if num >= n - 1:      
        ans = min(ans, calc())
        return 

    # 이동 조합 만들기 
    # (1, 2, 3, 4, 1 -> 0, 1, 2, 3, 0 으로 표현)
    for i in range(1, n):
        if not visited[i]:
            visited[i] = 1
            choice.append(i)
            choose(num + 1)
            visited[i] = 0
            choice.pop()

choose(0)
print(ans)