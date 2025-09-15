#클래스를 선언한다
class Student:
    pass
#학생을 선언한다
student = Student()
#학생 리스트를 선언
student = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
]

#클래스변수는 모든 객체가 참조하는 변수
#but 객체가 변수를 재할당받으면 해당 객체는 더이상 참조하지 않는다.