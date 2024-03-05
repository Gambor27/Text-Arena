from classes.colors import Colors

class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.current_hp = 100
        self.max_damage = 15
        self.min_damage = 5