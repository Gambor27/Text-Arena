from classes.colors import Colors
from classes.player import Player
from classes.locations import Location
from classes.game import Game


def build_room(room_id, name, exits, description, room_list):
    room = Location(name, exits, description)
    room_list[room_id] = room
   
def prompt(player, game):
    while 1 > 0:
        command = input(f"{Colors.fg.green}[{player.name}]:{Colors.reset}")
        if command == "exit":
            break
        player.move(command, game.rooms)

def main():
    game = Game()
    player = Player("Testman")
    build_room(0, 'starting_room', {"east" : 1}, "A small room", game.rooms)
    build_room(1, "other_room", {"west" : 0}, "Another small room", game.rooms)
    print(game.rooms[player.location].description)
    prompt(player, game)


main()