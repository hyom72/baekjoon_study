# 백준 문제(2021.5.27)
# 15726번) 다음과 같이 세 수가 연속해서 주어졌을 때 
# 한 번의 곱셈 기호와 한 번의 나눗셈 기호를 이용하여 만든 식 중 
# 가장 큰 값을 출력하는 프로그램을 작성하시오. 
# (세 수의 순서는 변하지 않는다.)

a, b, c = map(int, input().split())

result1 = a*b/c
result2 = a/b*c

print(int(max(result1, result2)))