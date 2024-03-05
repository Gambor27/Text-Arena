from classes.colors import Colors

class Player:
    def __init__(self, name):
        self.name = name
        self.location = 0
    
    def move(self, direction, room_list):
        current_room = room_list[self.location]
        if direction in current_room.exits:
            self.location = current_room.exits[direction]
            print(Colors.fg.cyan + Colors.bold +
                  room_list[self.location].name + "\n" + 
                  Colors.reset + 
                  room_list[self.location].description)
        else:
            print("You cannot go that way.")
    
    def look(self, room_list, direction=None):
        current_room = room_list[self.location]
        if direction in current_room.exits:
            print(Colors.fg.cyan + Colors.bold + 
                  room_list[current_room.exits[direction]].name + "\n" + 
                  Colors.reset + 
                  room_list[current_room.exits[direction]].description)
        elif direction is None:
            print(Colors.fg.cyan + Colors.bold + 
                  room_list[self.location].name + "\n" + 
                  Colors.reset + 
                  room_list[self.location].description)
        else:
            print(f"There is nothing to see to the {direction}.")