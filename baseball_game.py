from score import Score
from answer import ComAnswer, UserAnswer


class BaseBallGame:

    @staticmethod
    def start():
        score = Score(ComAnswer(), UserAnswer())
        score.announce()


if __name__ == "__main__":
    BaseBallGame().start()
