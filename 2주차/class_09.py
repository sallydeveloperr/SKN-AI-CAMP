#가위 바위 보 게임을 클래스로 구현하기
#사용자로부터 입력을 받아 컴퓨터와 대경하는 간단한 가위바위보 게임을 구현
#사용자는 가위바위보 중 하나를 입력하고 컴퓨터는 무작위로 선택
#게임의 승패를 판단하고 결과를 출력합니다
#가위는 1, 바위는 2, 보는 3으로 표현
#게임이 끝나면 사용자에게 다시 플레이할지 물어봅니다

import random

while True:
    class RPSGame:
        choices = {1: '가위', 2: '바위', 3: '보'}
        def __init__(self, user_choice):
            self.user_choice = None
            self.computer_choice = None
        def get_user_choice(self):
            while True:
                try:
                    choice = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                    if choice in self.choices:
                        self.user_choice = choice
                        break
                    else:
                        print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력하세요.")
                    