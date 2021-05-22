# 백준 문제(2021.5.20)
# 1330번) 첫째 줄에 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# A가  B보다 큰 경우 '>' 출력
# A가  B보다 작은 경우 '<' 출력
# A와 B가 같은 경우 '==' 출력

a, b = map(int, input().split())

if a > b :
    print(">")
elif a < b :
    print("<")
else :
    print("==")