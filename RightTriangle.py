# Prompt the user for a character
triangle_char = input("Enter a character:\n")

# Prompt the user for the triangle height
triangle_height = int(input("Enter triangle height:\n"))

print('')
# Loop through each line of the triangle
for i in range(triangle_height):
    # Print the user-specified character multiplied by the line number, with proper whitespace
    print((triangle_char + ' ') * (i + 1))