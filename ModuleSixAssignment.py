# Harrison LaBrecque

# The rooms variable represents the layout of the game, with each room mapped to the available directions to move to other rooms.
rooms = {'Great Hall': {'South': 'Bedroom'}, 'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
         'Cellar': {'West': 'Bedroom'}}

# The current_room variable is initially set to 'Great Hall' , representing the starting room.
current_room = 'Great Hall'

# The while loop continues as long as the current_room is not 'exit' .
while current_room != 'exit':
    # the player is informed about their current location.
    print('You are in the', current_room)
    command = input('Enter your command: ').lower()  # Convert command to lowercase
    # If the command starts with 'go' , it means the player wants to move in a certain direction
    if command.startswith('go'):
        # The command is split to extract the direction.
        direction = command.split()[1]
        # The direction is capitalized to match the keys in the rooms dictionary.
        if direction.capitalize() in rooms[current_room]:  # Convert direction to capitalized form
            # If the direction is valid for the current room, the current_room is updated to the corresponding room in that direction.
            current_room = rooms[current_room][direction.capitalize()]
        else:
            # If the direction is not valid, an error message is printed.
            print('Invalid direction!')
    # If the command is 'exit' , the loop is terminated by setting current_room to 'exit' .
    elif command == 'exit':
        current_room = 'exit'
    else:
        # If the command is neither 'go' nor 'exit' , an error message is printed.
        print('Invalid command!')

# After the loop, a final message is printed to thank the player for playing.
print('Thank you for playing!')
