# 백준 문제(2021.8.3)
# 2476번) https://www.acmicpc.net/problem/2476

n = int(input())
max_sum = 0
sum = 0

for i in range(n) :
    a, b, c = map(int, input().split())

    if(a!=b!=c) :
        sum = max(a, b, c)*100
    elif(a==b==c) :
        sum = 10000 + a*1000
    elif(a==b) :
        sum = 1000 + a*100
    elif(b==c) :
        sum = 1000 + b*100
    elif(a==c) :
        sum = 1000 + c*100

    if(max_sum < sum) :
        max_sum = sum

print(max_sum)
