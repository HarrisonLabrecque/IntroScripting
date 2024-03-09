#asking for user input.
user_input = input()
#Splitting the list.
tokens = user_input.split()
#creating an empty list to store the non-negative numbers.
numbers_list = []

#looping through the values in the list 'tokens'.
for token in tokens:
    #checking to see if the element in tokens is greater or equal to zero.
    if int(token) >= 0:
        #adding the value to the list 'number_list'.
        numbers_list.append(int(token))

#Sorting the elements in the list from lowest to greatest.
numbers_list.sort()

#printing the value of the list via a for loop.
for num in numbers_list:
    print(num, end=' ')