# 백준 문제(2021.5.23)
# 6763번) Many communities now have “radar” signs that tell drivers what their speed is, 
# in the hope that they will slow down.
# You will output a message for a “radar” sign. 
# The message will display information to a driver based on his/her speed according to the following table:

# km/h over the limit	Fine
# 1 to 20	            $100
# 21 to 30	            $270
# 31 or above	        $500

# output) If the driver is not speeding, the output should be:
# Congratulations, you are within the speed limit!
# If the driver is speeding, the output should be:
# You are speeding and your fine is $F.
# where F is the amount of the fine as described in the table above.

fine = int(input())
speed = int(input())
result = speed - fine

if(result <= 0) :
    print("Congratulations, you are within the speed limit!")
elif(1 <= result <= 20) :
    print("You are speeding and your fine is $100.")
elif(21 <= result <= 30) :
    print("You are speeding and your fine is $270.")
elif(result >= 31) :
    print("You are speeding and your fine is $500.")
