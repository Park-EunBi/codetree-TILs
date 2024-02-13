n = int(input())
customer = list(map(int, input().split()))

leader, member = map(int, input().split())
cnt = 0

for c in customer:
    # 팀장 
    c -= leader 
    cnt += 1
    if c <= 0:
        continue 

    # 팀원 
    cnt += (c // member)
    if c % member != 0:
        cnt += 1

print(cnt)