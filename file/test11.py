

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


#class methods

class Planet:
    name = "saturn"
    def __init__(self, name):
        self.name = name
    @classmethod
    def print_name(cls):
        print(cls.name)

alien = Planet("pluto")
print(alien.name)

alien.print_name()






