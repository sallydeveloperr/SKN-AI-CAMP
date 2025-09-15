#클래스
#클래스 변수 vs 인스턴스 변수

class StudentMng():
    name = '홍길동'
    def make_instance(self):
        self.age = 0
        self.addr = 0

s1 = StudentMng()
s2 = StudentMng()
s3 = StudentMng()

print(s1.name, s2.name, s3.name)
s1.name = '강감찬' #인스턴스 변수, but 현업에서 이렇게 객체가 인스턴스 변수를 수정하는 일은 없다 잘
StudentMng.name = '이순신'  #현업에서는 이렇게 클래스 변수를 수정하는 걸로 사용한다
print(s1.name, s2.name,s3.name)

#클래스변수는 모든 객체가 참조하는 변수
#but 객체가 변수를 재할당받으면 해당 객체는 더이상 참조하지 않는다.

