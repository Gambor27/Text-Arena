from classes.colors import Colors
import json

class Game:
    def __init__(self):
        self.rooms = {}
        self.enemies = []
        self.enemy_data = None
        self.current_location = 0
    

    def move(self, direction):
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            self.current_location = current_room.exits[direction]
            print(self.render_room_description(self.current_location))
            if self.current_location == 1 and self.enemies:
                print(self.render_enemies())
            print(self.render_directions())
        else:
            print("You cannot go that way.")
    
    def look(self, direction=None):
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            print(self.render_room_description(current_room.exits[direction]))
            if current_room.exits[direction] == 1 and len(self.enemies) > 0:
                print(self.render_enemies())
            print(self.render_directions())
        elif direction is None:
            print(self.render_room_description(self.current_location))
            if self.current_location == 1 and len(self.enemies) > 0:
                print(self.render_enemies())
            print(self.render_directions())
        else:
            print(f"There is nothing to see to the {direction}.")
    
    def render_room_description(self, room_id):
        return (Colors.fg.cyan + Colors.bold + 
                  self.rooms[room_id].name + "\n" + 
                  Colors.reset + 
                  self.rooms[room_id].description)
    
    def render_directions(self):
        current_room = self.rooms[self.current_location]
        exits = current_room.exits.keys()
        display = ""
        for exit in exits:
            display += exit + " "
        return f"{Colors.fg.light_blue} Exits: {Colors.reset} {display}"

    def render_enemies(self):
        also_here = ""
        for enemy in self.enemies:
            also_here += enemy.name + " "
        return(Colors.fg.purple + Colors.bold + "Also here: " + Colors.reset + Colors.fg.red + also_here + Colors.reset)