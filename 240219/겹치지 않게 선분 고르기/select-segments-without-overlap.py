n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

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