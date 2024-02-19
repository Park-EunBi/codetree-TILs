n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
selected_segs = list()

def overlapped(seg1, seg2):
    (ax1, ax2), (bx1, bx2) = seg1, seg2
    # 한 점이 다른 선분에 포함되는지 확인
    # 아래 등식에 하나라도 포함되면 안된다  
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

def possible():
    # 한 쌍이라도 겹치면 안됨 
    for i, seg1 in enumerate(selected_segs):
        for j, seg2 in enumerate(selected_segs):
            if i < j and overlapped(seg1, seg2):
                return False 
    return True

def find_max_segements(cnt):
    global ans
    if cnt == n:
        if possible():
            ans = max(ans, len(selected_segs))
        return 

    # 해당 라인을 포함했을 때 
    selected_segs.append(lines[cnt])
    find_max_segements(cnt + 1)
    selected_segs.pop()

    # 해당 라인을 포함하지 않았을 때 - append 안함
    find_max_segements(cnt + 1)

find_max_segements(0)
print(ans)

'''
# 틀림
import sys 
input = sys.stdin.readline

n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lines.sort()

choice_list = []
choice = []
maximum = 0
cnt = 0

def canMake(c):
    # 앞[1] >= 뒤[0] -> return False 
    for i in range(len(c) - 1):
        if lines[c[i]][1] >= lines[c[i + 1]][0]:
            return False
    return True 

def choose(num):
    if num == n:
        print(choice)
        if set(choice) not in choice_list:
            choice_list.append(set(choice))
        return 

    for i in range(n):
        choice.append(i)
        choose(num + 1)
        choice.pop()

choose(0)

for c in choice_list:
    if canMake(list(c)):
        maximum = max(maximum, len(c))

print(maximum)
'''

'''
7
491 696
500 967
311 878
53 720
634 728
380 570
55 682

2
'''