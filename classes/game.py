from classes.colors import Colors
import random

class Game:
    def __init__(self):
        self.rooms = {}
        self.enemies = []
        self.enemy_data = None
        self.current_location = 0
    

    def move(self, command):
        direction = command[0]
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            new_room = self.rooms[current_room.exits[direction]]
            self.current_location = current_room.exits[direction]
            self.spawn_enemies(command)
            print(self.render_room_description(self.current_location))
            if new_room.enemies:
                print(self.render_enemies())
            print(self.render_directions(self.current_location))
        else:
            print("You cannot go that way.")
    
    def look(self, command):
        direction = None
        if len(command) > 1:
            direction = command[1]
        current_room = self.rooms[self.current_location]
        if direction in current_room.exits:
            print(self.render_room_description(current_room.exits[direction]))
            if len(current_room.enemies) > 0:
                print(self.render_enemies())
            print(self.render_directions(current_room.exits[direction]))
        elif direction is None:
            print(self.render_room_description(self.current_location))
            if len(current_room.enemies) > 0:
                print(self.render_enemies())
            print(self.render_directions(self.current_location))
        else:
            print(f"There is nothing to see to the {direction}.")
    
    def spawn_enemies(self, command):
        current_room = self.rooms[self.current_location]
        if len(current_room.enemies) < current_room.max_enemies:
            enemy_index = random.randint(0,len(self.enemies) - 1)
            if enemy_index == len(self.enemies) - 1:
                new_enemy = self.enemies[enemy_index:]
            else:
                new_enemy = self.enemies[enemy_index:enemy_index + 1]
            current_room.enemies += new_enemy
    
    def render_room_description(self, room_id):
        return (Colors.fg.cyan + Colors.bold + 
                  self.rooms[room_id].name + "\n" + 
                  Colors.reset + 
                  self.rooms[room_id].description)
    
    def render_directions(self, room_id):
        current_room = self.rooms[room_id]
        exits = current_room.exits.keys()
        display = ""
        for exit in exits:
            display += exit + " "
        return f"{Colors.fg.light_blue} Exits: {Colors.reset} {display}"

    def render_enemies(self):
        also_here = ""
        current_room = self.rooms[self.current_location]
        for enemy in current_room.enemies:
            also_here += enemy.name + " "
        return(Colors.fg.purple + Colors.bold + "Also here: " + Colors.reset + Colors.fg.red + also_here + Colors.reset)