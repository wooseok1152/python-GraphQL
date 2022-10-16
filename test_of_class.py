class Person :

    name = "choi"

choi = Person()
kim = Person()
print(choi.name)
print(kim.name, "\n")

Person.name = "lee"
print(choi.name)
print(kim.name, "\n")