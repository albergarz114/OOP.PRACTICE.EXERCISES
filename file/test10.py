#Object Attributes

class Cat:
    def __init__(self, name):
        self.name = name

tom = Cat("Tom")
print(tom.name)

pamela = Cat("Pamela")
print(pamela.name)


#class Attributes

class Cat:

    number_of_legs = 4

tom = Cat()
print(tom.number_of_legs)

pamela = Cat()
print(pamela.number_of_legs)

Cat.number_of_legs = 2
print(tom.number_of_legs)



