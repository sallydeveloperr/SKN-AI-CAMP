#함수
#함수명 add
#파라미터는 2개 op1, op2
#결과를 반환한다

#생성
def add(op1, op2):
    result = op1 + op2
    return result

#사용
add(10, 20)

print( add(10,20) )
two_number_lab = add(10,30)
numbers = [add(10,2), add(100,20)]

#매개변수 받아서 출력하는 함수
#함수명 : show_number
#매개변수명 : data

def show_number(data):
    print(f'numbers = {data}')

show_number(add(10,2))


#다른 방법으로도 가능
def show_number(data):
    return(f'numbers = {data}')

print ( show_number(add(10,2)) )

#함수 만들어보기 예제
#매개변수로 "안녕하세요"라는 문자열을 받아서 그 안에서 len() 함수를 적용 → 문자열 길이(5)를 반환하는 함수를 만들기

def get_length(text):
    return len(text)

# 함수 호출
result = get_length("안녕하세요")
print(result)   # 출력: 5




























