#튜플
def change(obj):
    obj[0] = 100

data = [1,2,3]
change(data)
print(data)
print('-'*30)
a = 10
b = a
b = 1000
print(f'a={a} b = {b}')
print('-'*30)

list_a = [1,2,3]
list_b = list_a
list_b[0] = 100     #복사본 list_b의 내용값을 바꾼건데도 
print(f'list_a = {list_a} list_b = {list_b}')       #원본 list_a의 내용값도 바뀌었다
print('-'*30)
#리스트 안에 변수값은 하나밖에 못갖는다
#따라서 복사본의 변수값을 바꾼다고 해도 원본의 변수값도 바뀌는 것이다
#리스트는 주소값을 공유한다고 보면 된다 
#그게 원본 리스트이건 복사본 리스트이건!

list_c = [1,2,3]
list_b = list_c.copy()
list_b[0] = 100
print(f'list_c = {list_c} list_b = {list_b}') 