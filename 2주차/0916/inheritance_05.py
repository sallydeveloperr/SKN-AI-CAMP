#추상 클래스 사용하기
#@abstractmathod
#추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 
#강제하기 위해 사용한다.
#만약에 자식 클래스에서 해당 메서드를 오버라이드 하지 않으면
#아예 객체 생성 자체가 불가능하다
#따라서 해당 메서드는 자식들은 모두 갖고있어야한다.
#단 from abc import ABC를 필수로 해야 @abstractmethod 사용가능

from abc import ABC, abstractmethod
class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    
    @abstractmethod
    def save_money(self):
        pass

class Child(Parents):
    def make_money(self):  # 부모의 make_money 재정의(override)
        print('장사')   
    def save_money(self):
        print('투자')

c = Child()  # 부모의 추상메서드를 상속받으면 클래스에서 반드시 재 정의 안하면 객체 생성불가
c.make_money()  # 다형성   # 자식클래스에서 재 정의안하면 예외발생하도록 설계