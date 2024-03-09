# Get user inputs
key_value_pairs = input().split()
sentence = input()

# Convert key-value pairs to a dictionary
replace_dict = {key: value for key, value in zip(key_value_pairs[::2], key_value_pairs[1::2])}

# Replace words in the sentence
for orig, replace in replace_dict.items():
    sentence = sentence.replace(orig, replace)

# Print the modified sentence
print(sentence)