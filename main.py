from classes.colors import Colors
from classes.player import Player
from classes.locations import Location
from classes.game import Game
from classes.enemies import Enemy
import json

def build_room(room_id, name, exits, description, room_list):
    room = Location(name, exits, description)
    room_list[room_id] = room

def build_enemy(name, hp, hit_chance, min_damage, max_damage, armor, enemy_list):
    enemy = Enemy(name, hp, hit_chance, min_damage, max_damage, armor)
    enemy_list.append(enemy)

def load_file(filename, output):
    with open(filename, 'r') as data:
        data = json.load(data)
    return data[output]

def build_map(map_data, game):
        for room_id, room_data in map_data.items():
            build_room(int(room_id), room_data['name'], room_data['exits'], room_data['description'], game.rooms)

def populate_map(enemy_data, game):
    for enemy_stat in enemy_data:
        build_enemy(enemy_stat['name'], enemy_stat['hp'], enemy_stat['hit_chance'], enemy_stat['min_damage'], enemy_stat['max_damage'], enemy_stat['armor'], game.enemies)


def prompt(player, game):
    while 1 > 0:
        command = input(Colors.fg.green + 
                        f'[{player.name}]:' +
                        Colors.reset)
        parsed = command.split()
        if command == "exit":
            break
        elif parsed[0] == "look":
            if len(parsed) > 1:
                game.look(parsed[1])
            else:
                game.look()
        else:
            game.move(command)

def main():
    game = Game()
    player = Player("Testman")
    map_data = load_file("data/rooms.json", "rooms")
    enemy_data = load_file("data/enemies.json", "enemies")
    build_map(map_data, game)
    populate_map(enemy_data, game)
    print(game.render_room_description(game.current_location))
    prompt(player, game)


main()