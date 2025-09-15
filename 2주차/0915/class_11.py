#isinstance() 함수
# 객체가 특정 클래스의 인스턴스인지 확인하는 함수
#사용하는 이유 
#1. 객체의 타입을 확인하여 적절한 처리를 하기 위해
#2. 다형성을 구현할 때 객체가 특정 클래스의 인스턴스인지 확인하여 올바른 메서드를 호출하기 위해
#3. 오류 방지: 잘못된 타입의 객체가 전달되는 것을 방지하기 위해

class Student:
    def study(self):
        print("공부 중입니다.")
class Teacher:
    def teach(self):
        print("가르치는 중입니다.")

#리스트에 어떤 객체가 있는지 모를 때 특정 인스턴스만 기대할 수 없다.
people = [Student(), Teacher(), Student()]
del people[0]  #첫번째 학생 객체 삭제
if isinstance(people[0], Student):   #첫번째 객체가 학생인지 확인
    print(people[0].study())
else:                   #학생이 아니면 선생님이므로 teach() 메서드 호출                 
    print(people[0].teach())

