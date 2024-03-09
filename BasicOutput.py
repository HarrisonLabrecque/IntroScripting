#Asks the user to enter an integer.
user_num = int(input('Enter integer:\n'))

# Type your code here
#Squares the number entered in by the user.
number_squared = user_num ** 2
#Cubes the number entered in by the user.
number_cubed = user_num ** 3

#Prints the results to the screen.
print('You entered: {}'.format(user_num))
print('{0} squared is {1}'.format(user_num,number_squared))
print('And {0} cubed is {1} !!'.format(user_num,number_cubed))

#Asks the user to enter another integer.
user_num2 = int(input('Enter another integer:\n'))

#Adds the numbers entered in by the user.
addition = user_num + user_num2
#Mutliplies the numbers entered in by the user.
multiplication = user_num * user_num2

#Prints the results to the screen.
print('{0} + {1} is {2}'.format(user_num,user_num2,addition))
print('{0} * {1} is {2}'.format(user_num,user_num2,multiplication))
