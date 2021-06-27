# 백준 문제(2021.6.27)
# 3009번) https://www.acmicpc.net/problem/3009
x = []
y = []

for i in range(3) :
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3) :
    if(x.count(x[i]) == 1) :
        result_x = x[i]
for i in range(3) :
    if(y.count(y[i]) == 1) :
        result_y = y[i]
print(result_x, result_y)