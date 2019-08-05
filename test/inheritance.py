class Country:
    """super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')
    
class Korea(Country):
    """sub Class"""

    def __init__(self, name):
        self.name= name
    
    def show_name(self):
        print('국가 이름은 : ', self.name)


c1 = Korea('대한민국')
c1.show()
c1.show_name()
print(c1.capital)
print(c1.name)