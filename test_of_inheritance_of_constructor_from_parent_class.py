class test :

    def __init__(self, name) :

        self.name = name

class Person(test) :        # 'test'부모 클래스를 상속했기 때문에, test 클래스의 생성자 함수도 상속됨

    def print_name(self) :

        return self.name

a = Person("choi")          # 'test'클래스의 생성자 함수가 호출됨
print(a.print_name())