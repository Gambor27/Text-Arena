class Enemy:
    def __init__(self, name, hp, min_damage, max_damage, armor):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.armor = armor
