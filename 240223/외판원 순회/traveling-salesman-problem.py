n = int(input())
board= [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n + 1)]

ans = float('inf')

def calc():
    total = 0
    for j in range(len(choice) - 1):
        cost = board[choice[j]][choice[j + 1]]
        # 0은 이동할 수 없음
        if not cost:
            return float('inf') 
        total += cost
    return total

# 1에서 출발 (idx 처리 -> -1)
choice = [0]
def choose(num):
    global ans
    if num >= n - 1:   
        choice.append(0) # 1으로 되돌아 옴 (idx 처리 -> -1)
        ans = min(ans, calc())
        choice.pop() # 넣었던 것 다시 pop (조합 재 생성 위해)
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

'''
5
0 5 0 4 4 
5 0 8 8 8 
1 0 0 9 9 
3 8 8 0 6 
3 8 10 6 0 

27
'''