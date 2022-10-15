class test :

    def __init__(self, name) :

        self.name = name

class Person(test) :

    def print_name(self) :

        return self.name

a = Person("choi")
print(a.print_name())