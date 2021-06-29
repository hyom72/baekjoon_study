# 백준 문제(2021.6.29)
# 10871번) https://www.acmicpc.net/problem/10871

count, num = map(int, input().split())
li = list(map(int, input().split()))

for i in range(count) :
    if li[i] < num :
        print(li[i], end = " ")


