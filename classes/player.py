from classes.colors import Colors
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.current_hp = 100
        self.hit_chance = .75
        self.max_damage = 15
        self.min_damage = 5
        self.armor = 1

    def deal_damage(self):
        if random.randint(0,100) < (self.hit_chance * 100):
            return random.randint(self.min_damage, self.max_damage)
        else:
            return False
    
    def take_damage(self, source, damage):
        if damage:
            if damage < self.current_hp:
                self.current_hp -= (damage - self.armor)
                return [f'{Colors.fg.light_red}{source.name} strikes you for {damage} points of damage{Colors.reset}', True]
            elif damage > self.current_hp:
                self.current_hp = 1
                return [f'{Colors.bg.red}You have been defeated{Colors.reset}', False]
        else:
            return [f'{Colors.fg.cyan}{source.name} swings at you but misses{Colors.reset}', True]