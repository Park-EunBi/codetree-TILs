s = list(input())

# 오른쪽으로 shift
def shift():
    s.insert(0, s.pop())

# 압축
def encoding():
    result = ''
    cnt = 1

    if len(s) == 1:
        return 2
        
    for idx in range(len(s) - 1):
        if s[idx] == s[idx + 1]:
            cnt += 1
        else:
            result += str(s[idx] + str(cnt))
            cnt = 1
        
        if idx == len(s) - 2:
            result += str(s[idx + 1] + str(cnt))

    return len(result)


ans = float('inf')
for i in range(len(s)):
    shift()
    ans = min(ans, encoding())

print(ans)