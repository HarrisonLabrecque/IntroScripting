
# It defines a function called `process_input_file` that takes an `input_file` parameter.
def process_input_file(input_file):
    with open(input_file, 'r') as file:
        #Within the function, it opens the input file in read mode and reads all the lines into a list called `lines`.
        lines = file.readlines()
#It initializes an empty dictionary called `data_dict` to store the processed data.
    data_dict = {}
    #It iterates over the lines in the `lines` list, processing two lines at a time.
    for i in range(0, len(lines), 2):
        #It converts the first line (representing the number of seasons) to an integer.
        seasons = int(lines[i])
        #It strips the second line (representing the show names) of any leading or trailing whitespace.
        show_line = lines[i + 1].strip()
        # It splits the show names using the delimiter `;` and sorts them alphabetically.
        shows = sorted(show_line.split('; '))
        #It checks if the number of seasons already exists as a key in the `data_dict`. If not, it adds the seasons and corresponding shows as a new key-value pair.
        #If it exists, it appends the shows to the existing key.
        if seasons not in data_dict:
            data_dict[seasons] = shows
        else:
            data_dict[seasons].extend(shows)
    # It sorts the `data_dict` based on the keys in ascending order.
    sorted_keys = sorted(data_dict.items(), key=lambda x: x[0])
    #It opens a file called "output_keys.txt" in write mode and writes the sorted keys and corresponding shows to the file.
    with open("output_keys.txt", 'w') as file:
        for key, shows in sorted_keys:
            file.write(f"{key}: {'; '.join(shows)}\n")
    # It creates a list called `all_shows` by flattening the values of `data_dict` and sorting them alphabetically.
    all_shows = sorted([show for shows in data_dict.values() for show in shows])
    #It opens a file called "output_titles.txt" in write mode and writes all the show names to the file.
    with open("output_titles.txt", "w") as file:
        for show in all_shows:
            file.write(f"{show}\n")

# Read the input file name from user input
input_file = input()
process_input_file(input_file)