class Quest:
    def __init__(self, id, title, stage):
        self.id = id
        self.title = title
        self.stage = stage
        self.status = "Inactive"

    def start(self):
        self.status = "Active"

    def complete(self):
        self.status = "Complete"

    def is_active(self) -> bool:
        return self.status == "Active"