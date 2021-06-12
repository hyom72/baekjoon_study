# 백준문제(2021.6.11)
# 20673번) https://www.acmicpc.net/problem/20673

a = int(input())
b = int(input())

if(a <= 50 and b <= 10) :
    print("White")
elif(b >= 30) :
    print("Red")
else :
    print("Yellow")