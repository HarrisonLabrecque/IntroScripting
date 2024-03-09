#Asks for user input
user_input = input()
#Spliting the string into a list.
tokens = [int(i) for i in user_input.split()]
#taking the average.
average = int(sum(tokens) /len(tokens))
#finding the max value.
max_num = max(tokens)
#printing the result.
print(average, max_num)

    

