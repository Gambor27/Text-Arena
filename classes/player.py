from classes.colors import Colors
import random

class Player:
    def __init__(self, name, job, hp, hit_chance, max_damage, min_damage, armor):
        self.name = name
        self.job = job
        self.max_hp = hp
        self.current_hp = hp
        self.hit_chance = hit_chance
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.armor = armor
        self.exp = 0
        self.level = 1
        self.combat = ["fight","attack","a"]

    def deal_damage(self, command):
        if command[0] == "bash":
            if random.randint(0,100) < (self.hit_chance * 50):
                return random.randint(self.min_damage * 2, self.max_damage * 3)
            else:
                return False
        else:
            if random.randint(0,100) < (self.hit_chance * 100):
                return random.randint(self.min_damage, self.max_damage)
            else:
                return False
    
    def take_damage(self, source, damage):
        if damage:
            if damage < self.current_hp:
                self.current_hp -= (damage - self.armor)
                return [f'{Colors.fg.light_red}The {source.name} strikes you for {damage} points of damage{Colors.reset}', True]
            elif damage > self.current_hp:
                self.current_hp = 1
                return [f'{Colors.bg.red}You have been defeated!{Colors.reset}', False]
        else:
            return [f'{Colors.fg.cyan}The {source.name} swings at you but misses{Colors.reset}', True]
    
    def gain_exp(self, value):
        print(f"You gain {value} experience!")
        self.exp += value
        if self.exp >= (self.level * 100):
            self.level_up()
    
    def level_up(self):
        print(Colors.fg.light_blue + Colors.bold + "You have gained a level!" + Colors.reset)
        if (self.job == "fighter") & (self.level == 1):
            self.combat.append("bash")
        self.max_hp += 50
        self.current_hp = self.max_hp
        self.level += 1