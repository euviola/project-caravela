class CommandParser:
    def __init__(self):
        self.commands : dict[str, str] = {
            "Move": "on_character_move", "Look": "on_character_examine", "forest" : "location_forest"
            }
        self.command_keys = [key for key in self.commands.keys()]
        self.command_values = [value for value in self.commands.values()]

    #splits the command into separate words
    def SplitCommand(self, command:str):
        command_split = command.split()
        
        return command_split
    
    #analyzes the first argument (action): is it "move"? Maybe "look"?
    def ReturnFirstArgument(self, command_split:list):
        first_arg = command_split[0]

        for key in self.command_keys:
            if first_arg == key:
                return key, self.commands[key]
    
    #analyzes the second argument (data): if move, then where to?
    #note: omits the "to", "the", "at" arguments (therefore the slice [1:])
    def ReturnSecondArgument(self, command_split:list):
        second_arg = command_split[1:]

        for key in self.command_keys:
            for arg in second_arg:
                if arg == key:
                    return key, self.commands[key]