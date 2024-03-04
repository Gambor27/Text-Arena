from classes.colors import Colors
from classes.player import Player
from classes.locations import Location


def build_room(room_id, name, exits, description, room_list):
    room = Location(name, exits, description)
    room_list[room_id] = room
   
def prompt(player, room_list):
    while 1 > 0:
        command = input(f"{Colors.fg.green}[{player.name}]:{Colors.reset}")
        if command == "exit":
            break
        player.move(command, room_list)

def main():
    room_list = {}
    player = Player("Testman")
    build_room(0, 'starting_room', {"east" : 1}, "A small room", room_list)
    build_room(1, "other_room", {"west" : 0}, "Another small room", room_list)
    prompt(player, room_list)


main()