#object Attributes
class Dog:

    number_of_legs = 4
    def __init__(self, name):
        self.name = name

wishbone = Dog("wishbone")

print(wishbone.name)

milo = Dog("milo")

print(milo.name)


Dog.name = "Goofy" #results will be wishbone
print(wishbone.name)

# class Attributes

class Dog:
    number_of_legs = 4

wishbone = Dog()
print(wishbone.number_of_legs)

milo = Dog()
print(milo.number_of_legs)

Dog.number_of_legs = 3
print(wishbone.number_of_legs)


# Class methods

class Dog:
    name = "pluto"
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def print_name(cls):
        print(cls.name)

milo = Dog("milo")
print(milo.name)

milo.print_name()