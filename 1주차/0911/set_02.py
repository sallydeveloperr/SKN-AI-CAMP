#집합연산이 가능
#이 코드는 결국 list_a와 list_b의 교집합 요소를 find_list에 담는 코드
import random

# 0~9 사이에서 중복 없이 6개 뽑기
list_a = random.sample(range(10), 6)

# 0~9 사이에서 중복 없이 4개 뽑기
list_b = random.sample(range(10), 4)

find_list = []

# list_a의 각 원소 a와 list_b의 각 원소 b를 비교
for a in list_a:
    for b in list_b:
        if a == b:                # 같은 값이 있으면
            find_list.append(a)   # find_list에 추가


print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
print(f'find_list = {find_list}')
print(f'set( find_list )= {set(find_list)}')        #find_list 안에 있던 중복 원소들을 제거한 결과가 출력된다
