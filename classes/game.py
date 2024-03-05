from classes.colors import Colors

class Game:
    def __init__(self):
        self.rooms = {}
        self.enemies = []
        self.current_location = 0
    
    def get_enemies_at_location(self, room_id):
        return self.enemy_locations.get(room_id, [])
    
    def move(self, direction):
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            self.current_location = current_room.exits[direction]
            print(self.render_room_description(self.current_location))
            if self.current_location == 1 and len(self.enemies) > 0:
                also_here = ""
                for enemy in self.enemies:
                    also_here += enemy.name + " "
                print(Colors.fg.purple + Colors.bold + "Also here: " + Colors.reset + Colors.fg.red + also_here)
        else:
            print("You cannot go that way.")
    
    def look(self, direction=None):
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            print(self.render_room_description(current_room.exits[direction]))
            if current_room.exits[direction] == 1 and len(self.enemies) > 0:
                also_here = ""
                for enemy in self.enemies:
                    also_here += enemy.name + " "
                print(Colors.fg.purple + Colors.bold + "Also here: " + Colors.reset + Colors.fg.red + also_here)
        elif direction is None:
            print(self.render_room_description(self.current_location))
            if self.current_location == 1 and len(self.enemies) > 0:
                also_here = ""
                for enemy in self.enemies:
                    also_here += enemy.name + " "
                print(Colors.fg.purple + Colors.bold + "Also here: " + Colors.reset + Colors.fg.red + also_here)
        else:
            print(f"There is nothing to see to the {direction}.")
    
    def render_room_description(self, room_id):
        return (Colors.fg.cyan + Colors.bold + 
                  self.rooms[room_id].name + "\n" + 
                  Colors.reset + 
                  self.rooms[room_id].description)