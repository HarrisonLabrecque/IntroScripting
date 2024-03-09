#Asks the user for input.
user_input = input()
#Splitting the string into a list.
tokens = user_input.split()
#looping through the list 'tokens'.
for token in tokens:
    #prints the string from the list while counting how many times it shows up. 
    print(token,tokens.count(token))