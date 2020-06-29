class OutputView:

    @staticmethod
    def output_perfect_score():
        return print("3개의 숫자를 모두 맞추셨습니다! 게임을 종료합니다.")

    @staticmethod
    def output_score_counts(strike_cnt, ball_cnt):
        if not strike_cnt and not ball_cnt:
            print("0 스트라이크 0 볼")
        elif not ball_cnt:
            print("{} 스트라이크".format(strike_cnt))
        elif not strike_cnt:
            print("{} 볼".format(ball_cnt))
        else:
            print("{} 스트라이크 {} 볼".format(strike_cnt, ball_cnt))
        return


