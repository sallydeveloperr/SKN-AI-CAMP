#숫자 맞추기 게임
#규칙
#1. 컴퓨터가 1~100 사이의 숫자 하나를 랜덤으로 선택
#2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞추려고 시도
#3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "너무 높아요!" 출력
#4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "너무 낮아요!" 출력
#5. 사용자가 숫자를 맞추면 "정답입니다!" 출력하고 게임 종료
#6. 사용자가 숫자를 맞출 때까지 계속 시도할 수 있음

import random       #랜덤 모듈 임포트
class NumberGuessingGame:   #숫자 맞추기 게임 클래스 정의
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def guess_number(self):
        while True:
            try:
                user_guess = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
                self.attempts += 1
                if user_guess < 1 or user_guess > 100:
                    print("숫자가 범위를 벗어났습니다. 다시 시도하세요.")
                elif user_guess < self.number_to_guess:
                    print("너무 낮아요!")
                elif user_guess > self.number_to_guess:
                    print("너무 높아요!")
                else:
                    print(f"정답입니다! {self.attempts}번 만에 맞추셨네요.")
                    break
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하세요.")

gmame = NumberGuessingGame()
gmame.guess_number()