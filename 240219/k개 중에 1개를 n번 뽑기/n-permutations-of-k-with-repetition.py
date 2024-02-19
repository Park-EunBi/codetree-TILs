k, n = map(int, input().split())

answer = []
def choose(num): # parameter: 자릿수
    # 종료 조건 
    if num == n + 1:
        print(*answer)
        return 

    # 뽑기 
    for i in range(1, k + 1):
        answer.append(i)
        choose(num + 1)
        answer.pop()

choose(1)