# 백준 문제(2021.5.25)
# 11948번) JOI는 물리, 화학, 생물, 지구과학, 역사, 지리 총 6 과목의 시험을 봤다. 
# 각 시험의 만점은 100점이다.
# JOI는 물리, 화학, 생물, 지구과학 4과목 중에서 3 과목을 선택하고 
# 역사, 지리 2 과목 중에서 한 과목을 선택한다.
# 시험 점수의 합이 가장 높게 나오도록 과목을 선택할 때, 
# JOI가 선택한 과목의 시험 점수의 합을 구하시오.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

score1 = a+b+c+d-min(a, b, c, d)
score2 = max(e, f)

print(score1 + score2)