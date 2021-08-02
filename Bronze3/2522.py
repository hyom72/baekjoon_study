# 백준 문제(2021.8.3)
# 2522번) https://www.acmicpc.net/problem/2522

n = int(input())

for i in range(n-1, 0, -1) :
    print(i*" " + "*"*(n-i))

print("*"*n)

for i in range(n-1, 0, -1) :
    print((n-i)*" " + "*"*i)

