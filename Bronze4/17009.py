# 백준문제(2021.6.11)
# 17009번 ) The first three lines of input describe the scoring of the Apples, 
# and the next three lines of input describe the scoring of the Bananas. 
# For each team, the first line contains the number of successful 3-point shots, 
# the second line contains the number of successful 2-point field goals, 
# and the third line contains the number of successful 1-point free throws. 
# Each number will be an integer between 0 and 100, inclusive.
sum1 = 0
sum2 = 0

j = 3

for i in range(3):
    n = int(input())
    sum1 += n*j
    j -= 1

j = 3

for i in range(3) :
    n = int(input())
    sum2 += n*j
    j -= 1

if(sum1 < sum2) :
    print("B")
elif(sum1 > sum2) :
    print("A")
else :
    print("T")