# 백준 문제(2021.7.6)
# 1547번) https://www.acmicpc.net/problem/1547

n = int(input())
ball = [1, 0, 0, 0]

for i in range(n) :
    a, b = map(int, input().split())
    tmp = ball[b-1]
    ball[b-1] = ball[a-1]
    ball[a-1] = tmp
print(ball.index(1) + 1)