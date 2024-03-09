# Prompt the user to enter their favorite color, favorite noun, and favorite number
favorite_color = input()
favorite_noun = input()
favorite_number = input()

# Output the entered values on a single line
print("You entered: {} {} {}\n".format(favorite_color, favorite_noun, favorite_number))

# Create two password options
password1 = "_".join([favorite_color, favorite_noun])
password2 = "".join([favorite_number, favorite_color, favorite_number])

# Output the created passwords
print("First password:", password1)
print("Second password:", password2)

# Output the length of the password options
print("\nNumber of characters in", password1 + ":", len(password1))
print("Number of characters in", password2 + ":", len(password2))