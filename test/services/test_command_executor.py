from app.services.command_executer import CommandExecuter
import tqdm
import time


class TestCommandExecutor:
    def test_get_commands(self):
        command_executor_empty_commands = CommandExecuter()
        command_executor = CommandExecuter(commands=['echo', 'Hello!'])
        assert command_executor.commands == ['echo', 'Hello!']
        assert command_executor_empty_commands.commands == []