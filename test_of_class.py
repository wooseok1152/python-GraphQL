class Person :

    name = "choi"

choi = Person()
kim = Person()
print("!!! before defining variable of kim instance !!!", "\n")
print("* choi.name :", choi.name)
print("* kim.name :", kim.name, "\n")

print("!!! after defining variable of kim instance !!!", "\n")
kim.name = "kim"
print("* choi.name :", choi.name)
print("* kim.name :", kim.name)
print("* Person.name :", Person.name)