# 백준 문제(2021.6.27)
# 4766번) https://www.acmicpc.net/problem/4766
n_list= []

while(1) :
    n = float(input())
    if(n == 999) :
        break
    n_list.append(n)

for i in range(1, len(n_list)) :
    print("%.2lf" % (n_list[i] - n_list[i-1]))