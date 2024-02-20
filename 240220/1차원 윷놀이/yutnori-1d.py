n, m, k = map(int, input().split())
moves = list(map(int, input().split()))

choice = []
maximum = -1

def calc():
    score = [1 for _ in range(n)] # 모든 말은 1번 지점에서 시작
    cnt = 0
    for idx, c in enumerate(choice):
        score[c] += moves[idx]
    
    for s in score: 
        if s >= m:
            cnt += 1
    return cnt 
    
def choose(num):
    global maximum
    if num == n:
        maximum = max(maximum, calc())
        return 
    
    # 말 뽑기 
    for i in range(k):
        choice.append(i)
        choose(num + 1)
        choice.pop()

choose(0)
print(maximum)