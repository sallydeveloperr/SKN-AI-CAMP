class Product():
    serial_num = 0
    def __init__(self):
        Product.serial_num += 1
        self.serial_num = Product.serial_num
        self.name = None

if __name__ == 'main':
    tv1 = Product()
    tv2 = Product()
    tv3 = Product() 


""" h1 = People()
#make_instance()라는 메서드 안에서만 self.name, self.age, self.addr가 정의돼요.
#즉, 이 메서드를 호출하기 전까지는 h1 객체 안에는 addr 속성이 존재하지 않음.
print(h1.addr)
h2 = People()
print(h2.addr) """

