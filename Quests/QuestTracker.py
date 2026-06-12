from Engine.EventBus import EventBus
from Quest import Quest

class QuestTracker:
    def __init__(self):
        self.bus = EventBus()
        self.quests = {}

    def add(self, quest):
        self.quests[quest.id] = quest