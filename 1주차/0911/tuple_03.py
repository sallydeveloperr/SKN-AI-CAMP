#튜플->리스트
#리스트->튜플
list_a = [1,2,3]
tuple_a = (10,20,30)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')
print(tuple(list_a))
print(type(tuple(list_a)))      #리스트 자체가 튜플로 바뀐건 아니다

print('-'*30)

#리스트 자체를 튜플로 바꾸려면
list_a = tuple(list_a)
print(list_a)
