# 백준 문제(2021.5.22)
# 3004번) 상근이는 3003번에서 동혁이가 발견한 체스판을 톱으로 자르려고 한다.
# 상근이는 체스판을 최대 N번 자를 수 있으며, 변에 평행하게만 자를 수 있다. 
# 또, 자를 때는 체스판의 그 변의 한쪽 끝에서 다른쪽 끝까지 잘라야 한다. 
# 자른 후에는 조각을 이동할 수 없다.
# 이때, 최대 몇 조각을 낼 수 있는지 구하는 프로그램을 작성하시오.

n = int(input())

r = n//2
c = n-r
max_result = (r+1) * (c+1)

print(max_result)