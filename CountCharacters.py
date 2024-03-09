#The given code takes a string as input.
text = str(input())
#Assigns the first character of the string to the variable `character`
character = text[0]
#The remaining characters of the string to the variable `phrase`
phrase = text[1:]
#It then counts the occurrences of `character` in `phrase` and stores the count in the variable `count`.
count = phrase.count(character)
#Finally, it prints the value of `count`.
print(count)