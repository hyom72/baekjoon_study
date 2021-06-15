# 백준문제(2021.6.15)
# 8710번) https://www.acmicpc.net/problem/8710
import math

a, b, c = map(int, input().split())

d = b - a

print(math.ceil(d/c))
