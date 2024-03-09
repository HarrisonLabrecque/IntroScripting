word = ''

# Repeat until word is equal to 'quit'
while word != 'quit':
    # Prompt the user for input and split it into a list of strings
    user_input = input().split()
    
    # Store the first element of the user_input list in word variable
    word = user_input[0]

    # Check if the word is equal to 'quit'
    if word == 'quit':
        # Break out of the while loop if the word is 'quit'
        break

    # Store the second element of the user_input list in the number variable
    number = user_input[1]
    
    # Print a message using the number and word entered by the user
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))