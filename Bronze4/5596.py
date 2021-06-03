# 백준 문제(2021.6.3)
# 5596번

score1 = list(map(int, input().split()))
score2 = list(map(int, input().split()))

result1 = 0
result2 = 0

for i in range(4) :
    result1 += score1[i]
    result2 += score2[i]

if(result1 >= result2) :
    print(result1)
else :
    print(result2)
