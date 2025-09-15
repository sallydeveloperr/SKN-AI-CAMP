#다음 교시에 배울 것들
#enumerate(), zip(), .items(), .keys(), .values()
#map(), 함수의 파라미터 - 키워드파라미터, 가변 키워드 파라미터

""" #enumerate()        #튜플 형태로 출력된다
list_a = ['사과', '포도', '딸기']
for index, value in enumerate(list_a):
    print(f'{index} : {value}')

a, b = [10, 20] """

""" 
a,b = (0, '포도')
print(a)
print(b) """

i = (0, '포도')
print(i)

list_a = ['사과', '포도', '딸기']
for idx, data in enumerate(list_a):
    print(f'idx = {idx} data = {data}')

#zip() 두개의 리스트 또는 집합을 각 원소별로 묶어준다
names = ['홍길동', '이순신']
ages = [25, 35]
print(list(zip(names, ages)))
print(dict(zip(names, ages)))

for name, age in zip(names, ages):
    print(f'name:{names}, age:{ages}')

#.items() 는 딕셔너리의 메소드이다.
dict_1 = {'취미' : '수영', '좋아하는 음식' : '떡볶이'}

print(f'dict_1 = {dict_1}')
print(f'.keys() = {dict_1.keys()}')
print(f'.values() = {dict_1.values()}')
print(f'.items() = {dict_1.items()}')
