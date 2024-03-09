#Prompts user for input
input_month = input()
input_day = int(input())

#Checks to see if the month is March.
if input_month == 'March':
    #Checks to see if the date matches the given ranges then it sprints out the season. 
    if (1<= input_day <=19):
        print('Winter')
    elif (20 <= input_day <= 31):
        print('Spring')
    #Prints invalid if the date is out of the range.    
    else:
        print('Invalid')
#Checks to see if the month is April.        
elif input_month == 'April':
    #Prints the season if the date is the range.
    if (1 <= input_day <= 30):
        print('Spring')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is May.        
elif input_month == 'May':
    #Prints the season if the date is within this range.
    if (1 <= input_day <= 31):
        print('Spring')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is June.
elif input_month == 'June':
    #Checks to see if the date is within any of the given ranges then it prints out the season.
    if (1 <= input_day <= 19):
        print('Spring')
    elif (20 <= input_day <= 30):
        print('Summer')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is July.
elif input_month == 'July':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 31):
        print('Summer')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is August.
elif input_month == 'August':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 31):
        print('Summer')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is September.
elif input_month == 'September':
    #Checks the date to see if it is in the given ranges.
    if (1 <= input_day <= 20):
        print('Summer')
    elif (21 <= input_day <= 30):
        print('Autumn')
     #Otherwise, it prints invalid.     
    else:
        print('Invalid')
#Checks to see if the month is October.
elif input_month == 'October':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 31):
        print('Autumn')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is November.
elif input_month == 'November':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 30):
        print('Autumn')
    #Otherwise, it prints invalid.
    else:
        print('Invalid')
#Checks to see if the month is December.
elif input_month == 'December':
     #Checks the date to see if it is in the given ranges.
    if (1 <= input_day <= 20):
        print('Autumn')
    elif (21 <= input_day <= 31):
        print('Winter')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is January.
elif input_month == 'January':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 31):
        print('Winter')
    #Otherwise, it prints invalid.    
    else:
        print('Invalid')
#Checks to see if the month is February.
elif input_month == 'February':
    #Checks the date to see if it is in the given range.
    if (1 <= input_day <= 29):
        print('Winter')
    #Otherwise, it prints invalid.     
    else:
        print('Invalid')

else:
    print('Invalid')