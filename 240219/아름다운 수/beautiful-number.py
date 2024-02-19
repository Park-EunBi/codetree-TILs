n = int(input())

# 1, 2, 3, 4로 이루어진 n 자리 수 만들기 
number = []
cnt = 0

def is_beautiful():
    i = 0
    while i < n:
        # 남은 자리수가 현재 위치의 수로 만들 수 있는 최소 아름다운 수 보다 적을 때 
        # i: 3, n: 5, seq[i]: 4
        # xxx4x 현재 검사하는 수는 4라 아름다운 수가 되기 위해서는 최소 3자리가 더 필요함
        if i + number[i] - 1 >= n: 
            return False 

        for j in range(i, i + number[i]):
            if number[j] != number[i]: # 뒤에 나오는 수가 현재 나오는 수랑 다르면 
                return False 
        i += number[i]
    return True 

def count(num):
    global cnt
    # 탈출 조건
    if num == n:
        if is_beautiful():
            cnt += 1
        return 

    # 뽑기  
    for i in range(1, 5):
        number.append(i)
        count(num + 1)
        number.pop()

count(0)
print(cnt)