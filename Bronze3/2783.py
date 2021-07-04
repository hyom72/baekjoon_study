# 백준 문제(2021.7.4)
# 2783번) https://www.acmicpc.net/problem/2783

x, y = map(int, input().split())
min_price = x*(1000/y)

n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    if(x*(1000/y) < min_price) :
        min_price = x*(1000/y)

print("%.2lf" % min_price)

