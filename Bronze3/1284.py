# 백준 문제(2021.6.25)
# 1284번) https://www.acmicpc.net/problem/1284

sum = 0

while(1) :
    n = input()
    if(n == "0") :
        break
    sum += 1
    for i in (n) :
        if(i == "1") :
            sum += 2
        elif(i == "0") :
            sum += 4
        else :
            sum += 3
        sum += 1
    print(sum)
    sum = 0