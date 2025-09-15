#집합연산이 가능
#이 코드는 결국 list_a와 list_b의 교집합 요소를 find_list에 담는 코드
import random

list_a = random.sample(range(11), 7)    #0~10 중복되지 않는 임의의 7개
list_b = random.sample(range(11), 7)

#중복을 허용하면서 0~10까지 임의의 7 추출
#random.randint(0,10) -> 임의의 한개

list_c = []
for i in range(7):      #i의 역할이 없다
    list_c.append(random.randint(0,10))

"""
random.randint(0,10)
→ 0~10 사이에서 임의의 정수 하나를 뽑음 (중복 허용).
for i in range(7)
→ 7번 반복해서 list_c에 추가.
i 변수는 단순히 반복 횟수만 담당하고 실제로 쓰이지 않음. 
"""

#합집합
    #연산자 | (파이프 연산자)  --> 'or'
set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a | set_b
print(union_set)
    #매서드 .union()
set_a.union(set_b)
print(union_set)

print('-'*30)

#교집합
    #연산자 &  --> 'and'
set_a, set_b = {1,2,3,4}, {2,3,5}
print(set_a & set_b)
    #매서드 .intersection()
print(set_a.intersection(set_b))

print('-'*30)


#차집합
    #연산자 -
set_a, set_b = {1,2,3,4}, {2,3,5}
print(set_a - set_b)
    #매서드 .difference()
print(set_a.difference(set_b))