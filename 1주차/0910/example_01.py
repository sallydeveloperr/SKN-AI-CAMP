#가위바위보 게임 (컴퓨터 vs 휴먼)
#순환문 구조
#가위 : 1, 바위 : 2 ,보 : 3
#규칙 : 컴퓨터가 임의로 숫자를 선택 : random
#인간이 숫자를 입력 : input 
#승패를 기록
#3번마다 계속할 지 물어본다 : for문

import random
#1: 가위
#2: 바위
#3: 보
name = {1: "가위", 2: "바위", 3: "보"}

# 결과 집계
wins = losses = draws = 0

# 진행 제어( break 없이 )
continue_game = "Y"

# 진행 라운드 수
rounds = 0
#랜덤하게 선택한 컴퓨터의 값
com_choice = random.randint(1,3)

#사용자의 값
human_choice = int( input("당신의 선택은? (1:가위, 2:바위, 3:보) : ") )


def decide_winner(human, comp):
    """인간과 컴퓨터 선택(1/2/3)으로 승패 판정: 1=가위, 2=바위, 3=보"""
    if human_choice == com_choice:
        return "draw"
    # 가위(1) 이기려면 보(3), 바위(2) 이기려면 가위(1), 보(3) 이기려면 바위(2)
    if (human_choice == 1 and com_choice == 3) or (human_choice == 2 and com_choice == 1) or (human_choice == 3 and com_choice == 2):
        return "win"
    return "loss"


#승패 확인 
for rounds in range(0,100):
    result = decide_winner(human_choice, com_choice)
print(f"컴퓨터의 선택은? (1:가위, 2:바위, 3:보) :", com_choice)   #디버깅용..개발이 완료되면 삭제

if result == "win":
    wins += 1
    print( "당신이 이겼습니다!" )
elif result == "loss":
    losses += 1
    print( "당신이 졌습니다." )
else:
    draws += 1
    print( "비겼습니다." )



rounds += 1



if rounds % 3 == 0:
    print(f"\n[현재 전적] {rounds}판  승: {wins}  패: {losses}  무: {draws}")
    ans = input("계속하시겠습니까? To be continue (Y/y)? ").strip().upper()
    continue_game = "Y" if ans == "Y" else "N"
    print()  # 줄바꿈


#최종결과반환
print(f"게임 종료! 총 {rounds}판  |  승: {wins}  패: {losses}  무: {draws}")