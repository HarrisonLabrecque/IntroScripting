#The code receives input from the user and assigns it to the variable user_text.
user_text = input()
# Initialize count variable to 0
count = 0
# Iterate through each character in the user_text
for char in user_text:
    # Check if the character is not a space, period, or comma
    if char != " " and char != "." and char != ",":
        ## If condition is satisfied, increment the count by 1
        count += 1
#Prints the count
print(count)