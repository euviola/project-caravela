from gameobjects_base.gameobject_player.Player import Player
from gameobjects_base.Entity import Entity
from enginelayer.EventBus import EventBus

bus = EventBus()
player = Player(name="Stepan", race="Human", health=100)
test_entity = Entity(health=100, damage=15)

