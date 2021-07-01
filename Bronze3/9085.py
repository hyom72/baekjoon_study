# 백준 문제(2021.7.1)
# 9085번) https://www.acmicpc.net/problem/9085

n = int(input())

for i in range(n) :
    sum = 0
    num = int(input())
    li = list(map(int, input().split()))
    for i in range(num) :
        sum += li[i]
    print(sum)
