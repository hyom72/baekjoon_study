# 백준 문제(2021.6.9)
# 2753번) https://www.acmicpc.net/problem/2753
# 윤년 문제

a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)
