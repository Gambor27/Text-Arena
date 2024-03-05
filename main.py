from classes.colors import Colors
from classes.player import Player
from classes.locations import Location
from classes.game import Game
import json

def build_room(room_id, name, exits, description, room_list):
    room = Location(name, exits, description)
    room_list[room_id] = room
   
def prompt(player, game):
    while 1 > 0:
        command = input(f"{Colors.fg.green}[{player.name}]:{Colors.reset}")
        if command == "exit":
            break
        player.move(command, game.rooms)

def load_map(filename):
    with open(filename, 'r') as data:
        map = json.load(data)
    return map['rooms']

def main():
    game = Game()
    player = Player("Testman")
    map_data = load_map("data/rooms.json")
    for room_id, room_data in map_data.items():
        build_room(int(room_id), room_data['name'], room_data['exits'], room_data['description'], game.rooms)
    #print(game.rooms[player.location].description)
    print(f'{Colors.fg.cyan}{Colors.bold}{game.rooms[player.location].name} \n {Colors.reset}{game.rooms[player.location].description}')
    prompt(player, game)


main()