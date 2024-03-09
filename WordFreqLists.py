import csv
#Prompting the user to enter in the name of the file.
filename = input()
#A dictionary called `word_count` is initialized to store the word frequencies.
word_count = {}
# The `open()` function is used to open the specified file in read mode.
with open(filename, "r") as file:
    #The `csv.reader()` function is used to create a reader object to read the contents of the file.
    reader = csv.reader(file)
    #A nested loop is used to iterate over each row in the file and then over each word in the row.
    for row in reader:
        for word in row:
            #For each word encountered, the code checks if it already exists in the `word_count` dictionary.
            if word not in word_count:
                #If the word is not present, it is added to the dictionary with an initial count of 1.
                word_count[word] = 1
            else:
                #If the word is already present, its count is incremented by 1.
                word_count[word] += 1
#After processing all the words in the file, the `word_count.items()` method is used to iterate over the dictionary items.
for word, count in word_count.items():
    print(word, count)