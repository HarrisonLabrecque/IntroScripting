#Asking the user for input.
number1 = int(input())
number2 = int(input())
number3 = int(input())

#Checks to see if the value for number1 is less than the value for number2 and number3.
if number1 <= number2 and number1 <= number3:
    #prints the results.
    print(number1)
#CChecks to see if the value for number2 is less than the values for number1 and number3.
elif number2 <= number1 and number2 <= number3:
    print(number2)
#If the above conditions are not met, it means number3 is the smallest. 
else:
    print(number3)