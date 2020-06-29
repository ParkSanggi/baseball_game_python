from abc import *


class Player(metaclass=ABCMeta):

    def __init__(self):
        self.answer = self.set_answer()

    @abstractmethod
    def set_answer(self):
        pass


class ComputerPlayer(Player):
    def set_answer(self):
        answer = []
        while len(answer) != 3:
            pass


class UserPlayer(Player):
    def set_answer(self):
        pass



