# 백준 문제(2021.6.7)
# 2530번) https://www.acmicpc.net/problem/2530

h, m, s = map(int, input().split())
cookingsec = int(input())

s += cookingsec

m = m+int(s/60)
h = h+int(m/60)
h = h%24
m = m%60
s = s%60

print(h, m, s)