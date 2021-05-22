# 백준 문제(2021.5.22)
# 당신은 어떤 물건이라도 20% 할인해주는 쿠폰을 가지고 있다.
# 원래 가격이 주어질 때, 쿠폰을 사용하면 얼마가 되는지 알려주는 프로그램을 작성하시오.

# 첫 번째 줄에 테스트케이스의 수가 주어진다.
# 각 줄에는 물건의 원래가격이 소수점 둘째자리까지 주어진다.

n = int(input())
number = []

for i in range(n) :
    score = float(input())
    number.append(score)

for i in range(n) :
    print("$%.2f" %(number[i] - number[i]*(1/5)))