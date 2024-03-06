from classes.colors import Colors
from classes.player import Player
from classes.locations import Location
from classes.game import Game
from classes.enemies import Enemy
import json, time

def build_room(room_id, name, exits, description, room_list):
    room = Location(name, exits, description)
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
            build_room(int(room_id), room_data['name'], room_data['exits'], room_data['description'], game.rooms)

def populate_map(game):
    for enemy_stat in game.enemy_data:
        build_enemy(enemy_stat['name'], enemy_stat['hp'], enemy_stat['hit_chance'], enemy_stat['min_damage'], enemy_stat['max_damage'], enemy_stat['armor'], enemy_stat['value'], game.enemies)

def combat(command, player, game):
    combat_on = True
    for enemy in game.enemies:
        if command[1] == enemy.name:
            while combat_on == True:
                time.sleep(0.5)
                for enemy in game.enemies:
                    if command[1] == enemy.name:
                        player_damage = player.deal_damage()
                        enemy_result = enemy.take_damage(player_damage)
                        combat_on = enemy_result[1]
                        print(enemy_result[0])                        
                        if combat_on == False:
                            player.gain_exp(enemy.exp_value)
                            game.enemies.remove(enemy)                            
                            return
                    enemy_damage = enemy.deal_damage()
                    player_result = player.take_damage(enemy, enemy_damage)
                    combat_on = player_result[1]
                    print(player_result[0])
                    if combat_on == False:
                        return
    print(f"{command[1]} is not here")





def prompt(player, game):
    while 1 > 0:
        command = input(Colors.fg.green + f'[{player.name}: {Colors.reset} {player.current_hp} \\ {player.max_hp}]:')
        parsed = command.split()
        if command == "exit":
            break
        elif parsed[0] == "look":
            if len(parsed) > 1:
                game.look(parsed[1])
            else:
                game.look()
        elif parsed[0] == "fight":
            if game.current_location == 1:
                combat(parsed, player, game)
            else:
                print("There is nothing to fight here")
        else:
            if len(game.enemies) == 0:
                populate_map(game)
            game.move(command)

def main():
    game = Game()
    player = Player("Testman")
    map_data = load_file("data/rooms.json", "rooms")
    game.enemy_data = load_file("data/enemies.json", "enemies")
    build_map(map_data, game)
    print(game.render_room_description(game.current_location))
    prompt(player, game)


main()