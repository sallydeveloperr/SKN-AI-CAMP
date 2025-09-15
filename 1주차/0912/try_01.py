#오류
    #구문오류(syntax error) == 오타 == 프로그램 실행 전에 발생하는 오류 == 아예 실행 자체가 안됨
    #런타임 오류/예외(runtime error) == 문법적 오류 == 프로그램 실행 중에 발생하는 오류 
#예외처리(exception handling)
    #오류를 피해가는 행위를 예외처리라고 한다
    #조건문을 사용하는 방법
        #기본 예외 처리
    #try 구문을 사용하는 방법

#예외가 발생할 수 있는 코드
""" number_input_a = int(input("정수입력> "))   #숫자를 입력받습니다.

print("원의 반지름:", number_input_a)       #출력합니다.
print("원의 둘레:", 2 * 3.14 * number_input_a)
print("원의 넓이:", 3.14 * number_input_a * number_input_a) """


""" print(f'{num1} + {num2} = {calc_lists[0]}')
print(f'{num1} - {num2} = {calc_lists[1]}')
print(f'{num1} * {num2} = {calc_lists[2]}')
print(f'{num1} / {num2} = {calc_lists[3]}') """

try:         #예외가 발생할 가능성이 있는 코드
    num1, num2 = map(int, input('공백을 기준으로 두 개의 숫자를 입력 : ').split())
    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    print('1. 더하기', end = '\t')
    print('2. 빼기', end = '\t')
    print('3. 곱하기', end = '\t')
    print('4. 나누기', end = '\t')
    choice = int(input('원하는 결과를 입력하세요 '))
    print(f'결과는 = {calc_lists[choice - 1]}')
except:
    print('오류발생')   #예외가 발생했을 때 실행할 코드
else:
    pass  #예외가 발생하지 않았을 때 실행할 코드
    #이때 예외발생 가능성이 있는 코드만 try 구문에 넣고 나머지는 모두 else 구문으로 빼는 경우가 많음

finally:
    #무조건 실행할 코드
    #try 구문 중간에 return으로 탈출해도 finally 구문은 무조건 실행하고 넘어간다
    pass


print('프로그램 종료')