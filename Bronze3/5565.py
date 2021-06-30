# 백준 문제(2021.6.29)
# 5565번) https://www.acmicpc.net/problem/5565

sum = 0
total = int(input())

for i in range(9) :
    sum += int(input())
print(total - sum)