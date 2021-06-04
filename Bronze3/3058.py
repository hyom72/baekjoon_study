# 백준 문제(2021.6.4)
# 3058번) 7개의 자연수가 주어질 때, 이들 중 짝수인 자연수들을 모두 골라 그 합을 구하고, 
# 고른 짝수들 중 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어, 7개의 자연수 13, 78, 39, 42, 54, 93, 86가 주어지면 
# 이들 중 짝수는 78, 42, 54, 86이므로 그 합은 78 + 42 + 54 + 86 = 260 이 되고, 
# 42 < 54 < 78 < 86 이므로 짝수들 중 최솟값은 42가 된다.

num = int(input())

for i in range(num) :
    li_even = []
    sum = 0
    li = list(map(int, input().split()))
    for j in range(7) :
        if(li[j]%2 == 0) :
            li_even.append(li[j])
            sum += li[j]
    print(sum, min(li_even))

