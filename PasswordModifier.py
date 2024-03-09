#Asks the user to enter in the text
word = input()
password = ''
#The code then iterates through each character in the 'word' string.
#For each character, it checks if it matches any of the specified conditions.
for character in word:
    #If the character is 'i', it replaces it with an exclamation mark '!'.
    if character == 'i':    
        password += '!'
    #If the character is 'a', it replaces it with an at symbol '@'.    
    elif character == 'a':   
        password += '@'
    #If the character is 'm', it replaces it with an uppercase 'M'.    
    elif character == 'm':   
        password += 'M'
    #If the character is 'B', it replaces it with the number '8'.    
    elif character == 'B':   
        password += '8'
    #If the character is 'o', it replaces it with a period '.'
    elif character == 'o':   
        password += '.'
        
    else:
        #If the character does not match any of the conditions, it is appended as it is to the 'password' string. 
        password += character
#After iterating through all characters, the code prints the 'password' string followed by 'q*s'. '''
print(password + 'q*s')      
                      