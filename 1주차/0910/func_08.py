#간단한 함수
#함수 이름과 함수 내의 로직이 한 줄로 표현 가능한 함수들
def my_add(a,b):
    return a+b

#이걸 한 줄로 표현하기 위해 람다함수 사용 lambda
#람다함수
#간단한 함수를 즉석에서 만들 때 유용
#무조건 값을 리턴하는 함수
#return 키워드 사용 안함
test = lambda a,b: a+b #이거 자체가 위에 my_add(a,b)랑 같은것임
a, b = 10, 20
print(f'{a}+{b} = {my_add(a,b)}')
print(f'{a}+{b} = {test(a,b)}')
#람다는 언제쓰냐면 어떤 함수가 또다른 함수를 전달받을때 사용한다


