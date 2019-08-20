#!/usr/bin/python3


def showInstructions():
    print('''
            RPG Game
            --------
            Commands:
              go [direction]
              get [item]
    ''')

def showStatus():
    #print the players current status
    print('-----------------------------')
    print(f"You are in the {currentRoom}.")
    # print the current inventory
    print ("Inventory: " + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}.")
    print('-----------------------------')

#create inventory
inventory = []

#a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                'south': 'Kitchen',
                'east': 'Dining Room',
                'item': 'skeletonkey'
            },
            'Kitchen': {
                'north': 'Hall',
                'item': 'monster'
            },
            'Dining Room': {
                'west': 'Hall',
                'south': 'Garden',
                'item': 'cookies'
            },
            'Garden': {
                'north': 'Dining Room'
            }
        }

currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the players next 'move'
    #.split() breaks it up into a list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type go 'first'
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to teh new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            #display a useful msg
            print(f"You just picked up {move[1]}!")
            #delete the item from the room
            del rooms[currentRoom]['item']
        else:
            #tell them they cant get it
            print('Can\'t get ' + move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'cookies' in inventory:
            inventory.remove('cookies')
            del rooms[currentRoom]['item']
            print('The monster snatches your delicious cookies and escapes through a hole in the wall!')
        else:
            print("A monster has you! Game over.")
            break

    if currentRoom == 'Garden' and 'skeletonkey' in inventory:
        print('You use the Skeleton Key to open the rusty gate! You have escaped the house. You Win!')
