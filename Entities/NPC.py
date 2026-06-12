from Entities.Character import Character

class NPC(Character):
    def __init__(self, id, name, health):
        super().__init__(id, name, health)