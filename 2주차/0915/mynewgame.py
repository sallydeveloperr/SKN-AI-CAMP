#덧셈 퀴즈 게임
#랜덤한 두수의 덧셈 문제 출제
#사용자가 답 입력
#정답 여부 출력
#정답 맞추면 1점 획득
#기본적인 산술 연산과 random 모듈 사용법 익히기, 클래스와 메서드 활용한다
import random
class AdditionQuizGame:
    def __init__(self):
        self.score = 0

    def generate_question(self):
        self.num1 = random.randint(1, 100)
        self.num2 = random.randint(1, 100)

    def ask_question(self):
        while True:
            try:
                answer = int(input(f"{self.num1} + {self.num2} = ? "))
                return answer
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하세요.")

    def check_answer(self, user_answer):
        correct_answer = self.num1 + self.num2
        if user_answer == correct_answer:
            print("정답입니다!")
            self.score += 1
        else:
            print(f"틀렸습니다! 정답은 {correct_answer}입니다.")

    def play(self):
        while True:
            self.generate_question()
            user_answer = self.ask_question()
            self.check_answer(user_answer)
            print(f"현재 점수: {self.score}")
            play_again = input("다시 하시겠습니까? (y/n): ").strip().lower()
            if play_again != 'y':
                print(f"최종 점수: {self.score}. 게임을 종료합니다.")
                break