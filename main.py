from classes.colors import Colors
from classes.player import Player
from classes.locations import Location
from classes.game import Game
from classes.enemies import Enemy
import json, time

def build_room(room_id, name, exits, enemies, max_enemies, description, room_list):
    room = Location(name, exits, enemies, max_enemies, description)
    room_list[room_id] = room

def build_enemy(name, hp, hit_chance, min_damage, max_damage, armor, value, enemy_list):
    enemy = Enemy(name, hp, hit_chance, min_damage, max_damage, armor, value)
    enemy_list.append(enemy)

def load_file(filename, output):
    with open(filename, 'r') as data:
        data = json.load(data)
    return data[output]

def build_map(map_data, game):
        for room_id, room_data in map_data.items():
            build_room(int(room_id), room_data['name'], room_data['exits'], room_data['enemies'], room_data['max_enemies'], room_data['description'], game.rooms)

def populate_enemies(game):
    for enemy_stat in game.enemy_data:
        build_enemy(enemy_stat['name'], enemy_stat['hp'], enemy_stat['hit_chance'], enemy_stat['min_damage'], enemy_stat['max_damage'], enemy_stat['armor'], enemy_stat['value'], game.enemies)

def combat(command, player, game):
    combat_on = True
    current_room = game.rooms[game.current_location]
    for enemy in current_room.enemies:
        if command[1] == enemy.name:
            while combat_on == True:
                time.sleep(0.5)
                for enemy in current_room.enemies:
                    if command[1] == enemy.name:
                        player_damage = player.deal_damage()
                        enemy_result = enemy.take_damage(player_damage)
                        if enemy_result[0]:
                            print(enemy_result[0])
                        else:
                            print(f'An error occurred while processing damage to enemy, player damage was {player_damage}')
                            return
                        if not enemy_result[1]:
                            player.gain_exp(enemy.exp_value)
                            current_room.enemies.remove(enemy)   
                            enemy.current_hp = enemy.max_hp              
                            return
                    enemy_damage = enemy.deal_damage()
                    player_result = player.take_damage(enemy, enemy_damage)
                    print(player_result[0])
                    if not player_result[1]:
                        game.current_location = 3
                        player.current_hp = player.max_hp
                        print(Colors.fg.cyan + "You are dragged to the healer, who cures your wounds" + Colors.reset)
                        return
    print(f"{command[1]} is not here")

def prompt(player, game):
    running = 1
    while running == 1:
        full_command = getInput(player)
        first_command = full_command[0]
        if first_command in ["exit","quit","q","close"]:
            running = 0
        elif first_command in ["look", "l"]:
            game.look(full_command)
        elif first_command in ["fight","attack","a"]:
            if game.rooms[game.current_location].enemies:
                combat(full_command, player, game)
            else:
                print("There is nothing to fight here")
        elif first_command in ["north", "south", "east", "west"]:
            game.spawn_enemies(full_command)
            game.move(full_command)
        else:
            print(Colors.fg.light_red + "Unknown command")
            
def getInput(player):
    command = input(Colors.fg.green + f'[{player.name}: {Colors.reset} {player.current_hp} \\ {player.max_hp}]:')
    commandLower = command.lower()
    parsed = commandLower.split()
    return parsed

def main():
    game = Game()
    player = Player("Testman")
    map_data = load_file("data/rooms.json", "rooms")
    game.enemy_data = load_file("data/enemies.json", "enemies")
    build_map(map_data, game)
    populate_enemies(game)
    print(game.render_room_description(game.current_location))
    print(game.render_directions())
    prompt(player, game)


main()