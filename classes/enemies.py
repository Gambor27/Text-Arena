import random

class Enemy:
    def __init__(self, name, hp, hit_chance, min_damage, max_damage, armor):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.hit_chance = hit_chance
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.armor = armor

    def deal_damage(self):
        if random.randint(0,100) < (self.hit_chance * 100):
            return random.randint(self.min_damage, self.max_damage)