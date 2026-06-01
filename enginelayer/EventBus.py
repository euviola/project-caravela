class EventBus:
    def __init__(self):
        self.listeners: dict[str, list] = {} 

    def subscribe(self, event : str, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        
        self.listeners[event].append(callback)

    def emit(self, event, data=None):
        if event not in self.listeners:
            return
        
        for callback in self.listeners[event]:
            callback(data)