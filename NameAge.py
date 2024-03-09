# Created by Harrison LaBrecque

# Prompts the user to enter in their first name.
first_name = str(input('What is your name? '))
# Prompts the user to enter in their age.
age = int(input('What is your age? '))
# Displays the current year.
current_year = 2023
# Calculates the year of birth given the current year and the age of the person.
year_of_birth = current_year - age
# Prints the results to the screen.
print('Hello {0}! You were born in {1}.'.format(first_name, year_of_birth))
