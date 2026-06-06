class Entity:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, data):
        print(f"Entity attack: {data['Damage']}")