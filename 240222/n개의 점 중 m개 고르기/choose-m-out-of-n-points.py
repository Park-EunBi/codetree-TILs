n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

def calc(a, b):
    return (dots[a][0] - dots[b][0]) ** 2 + (dots[a][1] - dots[b][1]) ** 2

maximum = -float('inf')
tow_choice = []

def tow_choose(idx, num):
    global maximum
    if num == 2:
        # 3. 두 점 사이 거리의 최댓값 구하기 
        maximum = max(calc(tow_choice[0], tow_choice[1]), maximum)
        return 

    for i in range(idx, m):
        tow_choice.append(choice[i])
        tow_choose(i + 1, num + 1)
        tow_choice.pop()

minimum = float('inf')
choice = []
# 1. 점 m 개 선택하기 
def choose(idx, num):
    global maximum, minimum
    if num == m:

        # 2. 선택된 점 중 2개 고르기 
        tow_choose(0, 0)
        
        # 4. 최댓값 중 최솟값 구하기
        minimum = min(minimum, maximum)
        maximum = -float('inf')

        return  

    for i in range(idx, n):
        choice.append(i)
        choose(i + 1, num + 1)
        choice.pop()

choose(0, 0)
print(minimum)