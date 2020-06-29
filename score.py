from output_view import OutputView


class Score:
    def __init__(self, correct, submit):
        self.strike_count = correct.get_strike_count(submit)
        self.ball_count = correct.get_ball_count(submit)
        self.perfect = correct.is_equal(submit)
        self.announce()
        print(correct._answer)
        print(submit._answer)

    def announce(self):
        if self.perfect:
            return OutputView.output_perfect_score()
        return OutputView.output_score_counts(self.strike_count, self.ball_count)

    def is_perfect(self):
        return self.perfect


