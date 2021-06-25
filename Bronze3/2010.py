# 백준 문제(2021.6.25)
# 2010번) https://www.acmicpc.net/problem/2010

import sys

n = int(sys.stdin.readline())
sum = 0

for i in range(n) :
    num = int(sys.stdin.readline())
    sum += num

print(sum - (n-1))