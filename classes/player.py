from colors import Colors

class Player:
    def __init__(self, name):
        self.name = name
        self.location = 0
    
    def move(self, direction, room_list):
        current_room = room_list[self.location]
        if direction in current_room.exits:
            self.location = current_room.exits[direction]
            print(self.location.description)
            #call player prompt
        else:
            print("You cannot go that way.")