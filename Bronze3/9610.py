# 백준 문제(2021.7.2)
# 8932번) https://www.acmicpc.net/problem/9610

n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
ax = 0

for i in range(n) :
    a, b = map(int, input().split())
    if(a == 0 or b == 0) :
        ax+=1
    elif(a > 0 and b > 0) :
        q1+=1
    elif(a < 0 and b > 0) :
        q2+=1
    elif(a < 0 and b < 0) :
        q3+=1
    elif(a > 0 and b < 0) :
        q4+=1
print("Q1: %d"%q1)
print("Q2: %d"%q2)
print("Q3: %d"%q3)
print("Q4: %d"%q4)
print("AXIS: %d"%ax)


