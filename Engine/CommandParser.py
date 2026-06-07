class CommandParser:
    def __init__(self):
        self.commands : dict[str, str] = {
            "Move": "on_character_move", "Look": "on_character_examine"
            }
        self.command_keys = [key for key in self.commands.keys()]
        self.command_values = [value for value in self.commands.values()]


    def SplitCommand(self, command:str):
        command_split = command.split()
        
        return command_split
        
    def ReturnFirstArgument(self, command_split):
        first_word = command_split[0]

        for key in self.command_keys:
            if first_word == key:
                return key, self.commands[key]