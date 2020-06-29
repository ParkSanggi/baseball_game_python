from score import Score
from answer import ComAnswer, UserAnswer


class BaseBallGame:

    @staticmethod
    def start():
        correct_answer = ComAnswer()
        submitted_answer = UserAnswer()
        score = Score(correct_answer, submitted_answer)
        while not score.is_perfect():
            submitted_answer = UserAnswer()
            score = Score(correct_answer, submitted_answer)


if __name__ == "__main__":
    BaseBallGame().start()
