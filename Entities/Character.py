from Entities.Entity import Entity

class Character(Entity):
    def __init__(self, id, name, health:int, is_alive:bool=True):
        super().__init__(id, name)
        self.health = health
        self.is_alive = is_alive