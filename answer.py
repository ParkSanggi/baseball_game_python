from abc import *
from random import *


class Answer:
    _LENGTH = 3

    def __init__(self):
        self._answer = []

    def get_answer(self):
        return self._answer

    def _is_valid(self, temp_answer):
        if len(temp_answer) != self._LENGTH or not temp_answer.isdigit():
            return False
        return True

    def is_equal(self, answer):
        return self._answer == answer.get_answer

    def get_ball_count(self, answer):
        res = 0
        target = answer.get_answer()
        for i in range(self._LENGTH):
            if self._answer[i] in target and self._answer[i] != target[i]:
                res += 1
        return res

    def get_strike_count(self, answer):
        res = 0
        target = answer.get_answer()
        for i in range(self._LENGTH):
            if self._answer[i] == target[i]:
                res += 1
        return res


class ComAnswer(Answer):

    def __init__(self):
        super().__init__()
        while len(self._answer) < self._LENGTH:
            num = randint(1, 9)
            if num not in self._answer:
                self._answer.append(num)


class UserAnswer(Answer):

    def __init__(self):
        super().__init__()
        temp_answer = ""
        while not self._is_valid(temp_answer):
            temp_answer = input()
        for num in temp_answer:
            self._answer.append(int(num))


