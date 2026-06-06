class Player:
    def __init__(self, name, race, health = 100):
        self.name = name
        self.race = race
        self.health = health
        
    def changeHealth(self, data):
        self.health -= data['Damage']

    def attack(self, data):
        print(f"attack: {data['Damage']}")