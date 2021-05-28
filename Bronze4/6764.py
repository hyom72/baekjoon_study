# 백준 문제(2021.5.23)
# 6764번 output) The output is one of four possibilities. 
# If the depth readings are increasing, then the output should be Fish Rising. 
# If the depth readings are decreasing, then the output should be Fish Diving. 
# If the depth readings are identical, 
# then the output should be Fish At Constant Depth. Otherwise, 
# the output should be No Fish.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a<b<c<d) :
    print("Fish Rising")
elif(a>b>c>d) :
    print("Fish Diving")
elif(a==b==c==d) :
    print("Fish At Constant Depth")
else :
    print("No Fish")