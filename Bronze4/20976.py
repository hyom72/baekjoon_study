# 백준문제(2021.6.21)
# 20976번) 입력받은 세 수 중 두 번째로 큰 수 출력

li = list(map(int, input().split()))

li.sort()

print(li[1])