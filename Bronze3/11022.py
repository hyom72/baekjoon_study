# 백준 문제(2021.7.7)
# 11022번) https://www.acmicpc.net/problem/11022
num = int(input())

for i in range(1, num+1) :
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i, a, b, a+b))