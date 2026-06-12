class Quest:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.stages = data["stages"]
        self.current_stage_index = 0
        self.completion_conditions = data["completion_condition"]
        self.status = data["status"]

    @property
    def current_stage(self):
        if self.status == "completed":
            return None
        return self.stages[self.current_stage_index]

    @property    
    def objective(self):
        if self.status == "completed":
            return None
        return self.current_stage["description"]
    
    def start(self):
        self.status = "active"
        print(f"Новий квест: {self.title}")
        print(f"{self.objective}")

    def check(self, event, data):
        if self.status != "active":
            return
        
        condition = self.current_stage["completion_condition"]

        if event != condition["event"]:
            return
        
        for key, value in condition.items():
            if key == "event":
                continue
            if data.get(key) != value:
                return
        
        self.advance()

    def advance(self):
        self.current_stage_index += 1

        if self.current_stage_index >= len(self.stages):
            self.status = "completed"
            print(f"Quest: {self.title} is completed")
        else:
            print(f"{self.objective}")