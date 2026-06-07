from Engine.CommandParser import CommandParser

cp = CommandParser()

command = "Move to the forest"
command_split = cp.SplitCommand(command)

print(cp.ReturnFirstArgument(command_split))
print(cp.ReturnSecondArgument(command_split))
