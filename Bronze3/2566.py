# 백준 문제(2021.6.28)
# 2566번) https://www.acmicpc.net/problem/2566

x = 0
y = 0
max_number = 0

for i in range(9) :
    li = list(map(int, input().split()))
    for j in range(9) :
        if(li[j] > max_number) :
            max_number = li[j]
            x = i + 1
            y = j + 1
print(max_number)
print(x, y)
