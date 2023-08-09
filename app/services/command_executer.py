import abc
import subprocess

class CommandExecuter(metaclass=abc.ABCMeta):
    commands: list[str]

    def __init__(self, commands: list[str] = None) -> None:
        self.commands = commands

        if not self.commands:
            self.commands = []

    def add_command(self, command: str):
        self.commands.append(command)

    def execute_command(self, cmd: str | list[str]):
        if type(cmd) == str:
            cmd = cmd.split(' ')

        result = subprocess.run(cmd)
        return result

