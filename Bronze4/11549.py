# 백준문제(2021.6.14)
# 11549번) The first line contains an integer T representing the tea type (1 ≤ T ≤ 4). 
# The second line contains five integers A, B, C, D and E, indicating the answer given 
# by each contestant (1 ≤ A, B, C, D, E ≤ 4).
# Output a line with an integer representing the number of contestants 
# who got the correct answer.

n = int(input())
answer = list(map(int, input().split()))
cnt = 0

for i in range(5) :
    if(n == answer[i]) :
        cnt += 1
print(cnt)
