#매개변수 있고 반환값 있는 형태
import time
def say_hello_name(name):
    print(f'{name}님 안녕하세요')
    return time.time()   # 호출 시점의 timestamp 반환


#매개변수 있고 반환값 없는 형태
def say_hello_name_only(name):
    print(f'{name}님 안녕하세요')

#매개변수 없고 반환값 있는 형태
import datetime
def get_rightnow_time():
    return datetime.datetime.now()


#매개변수 없고 반환값 없는 형태
def say_goodbye():
    print('안녕히가세요...')

#----------------------------------------
#함수를 활용해봅시다.

print(say_hello_name("유정"))   # 인사 + timestamp 반환
say_hello_name_only("유정")     # 인사만
print(get_rightnow_time())      # 현재 시간 반환
say_goodbye()                   # 작별 인사만

