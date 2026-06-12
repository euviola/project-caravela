from Engine.EventBus import EventBus
from Quest import Quest

class QuestTracker:
    def __init__(self):
        self.bus = EventBus()
        self.quests = {}

    def add(self, quest):
        self.quests[quest.id] = quest

    def on_npc_talked(self, data):
        if data["npc_id"] == "demo_npc_1" and "demo_quest_1" in self.quests:
            quest = self.quests["testquest"]
            if quest.status == "Inactive":
                quest.start()

    def on_killed_rat(self, data):
        kill_counter = 0
        if data["entity_id"] == ["demo_rat"] and "demo_quest_1" in self.quests:
            kill_counter += 1
            if kill_counter == 3:
                