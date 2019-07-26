class Student:
    def __init__(self, name):
        self.name=name
        
class GraduateStudent(Student):
    def __init__(self,name, major):
        super().__init__(name)
        self.major = major
        
s1 = Student('홍길동')
gs1 = GraduateStudent('이순신', '컴퓨터')
print(f'이름: {s1.name}')
print(f'이름: {gs1.name}, 전공: {gs1.major}')