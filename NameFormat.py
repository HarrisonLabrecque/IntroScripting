#Asks the user for their entire name.
full_name = input()
#Splits their name into elements which is stored in a list called 'names'.
names = full_name.split()
#Assigning the variable 'last_name' to the last element of names.
last_name = names[-1]

#Checking to see if the list 'names' has 3 elements.
if len(names) == 3:
    #Indexing to the first element in the list 'names' then to the first letter in that string.
    first_initial = names[0][0]
    #Indexing to the second element in the list 'names' then to the first letter in that string.
    middle_initial = names[1][0]
    #Printing the results to the screen.
    print('{0}, {1}.{2}.'.format(last_name,first_initial,middle_initial))
else:
    #Indexing to the first element in the list 'names' then to the first letter in that string.
    first_initial = names[0][0]
    #Printing the results to the screen.
    print('{0}, {1}.'.format(last_name,first_initial))

