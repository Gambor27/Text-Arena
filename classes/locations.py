class Location:
    def __init__(self, name, exits, enemies, max_enemies, description):
        self.name = name
        self.exits = exits
        self.enemies = enemies
        self.max_enemies = max_enemies
        self.description = description