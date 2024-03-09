# Created by Harrison Labrecque

#Displays the possible commands that the player can enter.
def display_commands():
    print('Possible commands:')
    print('go [direction]: Move to a different room (e.g., go north)')
    print('get [item]: Collect an item from the current room (e.g., get apple)')

#Displays the player's current status, including the current room, inventory, and items in the room.
def display_status(player, current_room, rooms):
    print('You are currently in', current_room)
    print('Inventory:', player["inventory"])
    if current_room in rooms:
        print("Items in this room:", rooms[current_room]["items"])

#Prompts the user to enter a command and returns the lowercase command string.
def get_command():
    command = input('Enter your command: ').lower()
    return command

#Moves the player to a different room based on the specified direction.
def move_player(player, direction, rooms):
    current_room = player['current_room']
    if direction in rooms[current_room]:
        player['current_room'] = rooms[current_room][direction]
    else:
        print('Invalid direction. Try again.')
#Collects an item from the current room, adds it to the player's inventory, and removes it from the room's item list.
def collect_item(player, item, rooms):
    current_room = player['current_room']
    if item in rooms[current_room]['items']:
        player['inventory'].append(item)
        rooms[current_room]['items'].remove(item)
        print('You have acquired', item)
    else:
        print('Item not found. Try again.')

#Checks if the player has reached the villain's room and collected all the required items to determine if the game is over.
def check_game_status(player, items_to_collect, villain_room):
    if player['current_room'] == villain_room:
        if len(player['inventory']) == len(items_to_collect):
            print('Congratulations! You have collected all the items and defeated the villain. You win!')
        else:
            print('You have encountered the villain before collecting all the items. You lose!')
        return True
    return False

#The main function that sets up the initial player state, room descriptions, and item locations.
#It handles the game loop, displaying the status and possible commands, getting and processing player input, and checking the game status to decide if the game is over.    
def main():
    #player is a dictionary that represents the player's current state. It contains the keys "current_room" and "inventory".
    #The player starts in the "grand foyer" room with an empty inventory.
    player = {
        "current_room": "grand foyer",
        "inventory": []
    }
#rooms is a nested dictionary that represents the different rooms in the game.
#Each room is a key in the rooms dictionary and contains a dictionary with keys "description", "items", and the possible directions to other rooms (north, south, east, west).
#Each room also has a description and may or may not have items.
    rooms = {
        "grand foyer": {
            "description": "You are in a dark room.",
            "items": None,
            "north": "kitchen",
            "west":"bedroom",
            "south":"cellar",
            "east":"dining room"
            },
        "kitchen": {
            "description": "You are in a messy kitchen.",
            "items": ["journal"],
            "south": "grand foyer",
            "east": "study room"
        },
        "dining room": {
            "description": "You are in a grand dining room.",
            "items": ["flashlight"],
            "west": "grand foyer",
            "south": "garden"
        },
        "garden": {
            "description": "You are in a beautiful garden.",
            "items": ["flower"],
            "north": "dining room"
        },
        "study room":{
        "description":"Papers are scattered everywhere.",
        "items":["medallion"],
        "west":"kitchen"
        },
        "bedroom":{
        "description": "There is mold on the walls!",
        "items":["photo"],
        "east":"grand foyer",
        "north":"attic"
        },
        "attic":{
        "description":"There is furniture covered in drapes",
        "items":["keys"],
        "south":"bedroom"
        },
        "cellar":{
        "description":"It is cold and damped down here!",
        "items": None,
        "north":"grand foyer",
        "west":"storage room"
        },
        "storage room":{
        "description":"Morgana is here?!",
        "items":["Morgana"],
        "east":"cellar"
        }
        
    }
#villain_room is set to "hidden room", which is the room where the villain is located.    
    villain_room = "storage room"
#items_to_collect is a list that contains the names of the items that the player needs to collect.
#The player must collect all these items before reaching the villain room to win the game. 
    items_to_collect = ["flashlight", "journal","flower","keys","photo","medallion"]
#game_over is initialized as False.
    game_over = False
#The while loop runs until the game is over.
    while not game_over:
#display_status function to show the player's current status
        display_status(player, player["current_room"], rooms)
        #display_commands shows the available commands
        display_commands()
        #get_command gets the player's input.
        command = get_command()
#If the player enters "quit", the game ends and "Thanks for playing! Goodbye!" is printed.
        if command == "quit":
            print("Thanks for playing! Goodbye!")
            break
#If the player enters a command that starts with "go", it calls the move_player function to move the player to the specified direction using the rooms dictionary.            
        if command.startswith("go"):
            direction = command.split()[1]
            move_player(player, direction,rooms)
#If the player enters a command that starts with "get", it calls the collect_item function to pick up the specified item from the current room using the rooms dictionary.
        if command.startswith("get"):
            item = command.split()[1]
            collect_item(player, item,rooms)
#it checks the game status using the check_game_status function.
#If the player has reached the villain room and collected all the required items, the game is over and the loop ends.
        if check_game_status(player,items_to_collect,villain_room):
#Finally, if the game_over flag is True, the while loop ends and the game is finished.
            game_over = True
#The main function is called if the script is run as the main module.
if __name__ == "__main__":
	main()
