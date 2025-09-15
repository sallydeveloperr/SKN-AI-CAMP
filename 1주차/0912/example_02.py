def get_data(start, end, input_str='입력'):
    while True:
        try:
            h_num = int(input(f"{input_str}({start}~{end}) : "))
            if not start <= h_num <= end:
                raise ValueError(f'{start} ~ {end} 범위 초과')
        except Exception as e:
            print(f'오류 : {e}')
        else:
            return h_num
        
#랜덤 정수 - 컴퓨터가 선택한 값
import random as rd
start, end = (1, 100)
computer = rd.randint(start, end)
count = 0
game_history = []
while True:
    count += 1
    human = get_data(start, end)

    #게임
    #human > computer --> "크다"
    #human < computer --> "작다"
    #human = computer --> "정답"

    if human > computer:
        print('정답보다 크다')
        game_history.append((human, '크다'))
    elif human < computer: 
        print('정답보다 작다')
        game_history.append((human, '크다'))

    else: 
        print(f'정답!! , 시도 횟수 : {count}')
        for idx, (guess_value, state) in enumerate(game_history, start=1):  # ✅ enumerate 사용
            print(f'{idx}번째 시도 : {guess_value} - {state}')
        break

