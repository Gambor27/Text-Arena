from classes.colors import Colors
from classes.game import Game

class Command:
    def __init__(self):
        self.index = ["look"]
        self.look = "game.look(full_command)"