class Quest:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.stages = data["stages"]
        self.current_stage = self.stages["start"]
        self.completion_conditions = data["completion_conditions"]
        self.status = data["status"]

    def start(self):
        self.status = "Active"

    def complete(self):
        self.status = "Complete"

    def is_active(self) -> bool:
        return self.status == "Active"