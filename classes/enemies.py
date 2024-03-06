import random
from classes.colors import Colors

class Enemy:
    def __init__(self, name, hp, hit_chance, min_damage, max_damage, armor, value):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.hit_chance = hit_chance
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.armor = armor
        self.exp_value = value

    def deal_damage(self):
        if random.randint(0,100) < (self.hit_chance * 100):
            return random.randint(self.min_damage, self.max_damage)
        else:
            return False
    
    def take_damage(self, damage):
        if damage:
            damage_inflicted = damage - self.armor
            if damage < self.current_hp:
                self.current_hp -= (damage - self.armor)
                return [f'{Colors.fg.light_red}You hit {self.name} for {damage} points of damage{Colors.reset}', True]
            elif damage > self.current_hp:
                return [f'{Colors.fg.blue}You have defeated {self.name}{Colors.reset}', False]
        else:
            return [f'{Colors.fg.cyan}You swing at {self.name} you but miss{Colors.reset}', True]