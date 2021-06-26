# 백준 문제(2021.6.26)
# 2455번) https://www.acmicpc.net/problem/2455
people = 0
max_people = 0

for i in range(4) :
    a, b = map(int, input().split())
    people = people - a
    people = people + b
    if(people > max_people) :
        max_people = people
print(max_people)
