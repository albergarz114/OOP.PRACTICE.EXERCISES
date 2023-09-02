class Building:

    def __init__(self, type, birth, age):
        self.type = type
        self.birth = birth
        self.age = age

class Office(Building):
    def my_bus(self):
        print("It is a good business and services")

class House(Building):
    def my_crib(self):
        print("What are you doing in my crib homie? ")

my_prop = Office("cement", "1996", "27")
my_loc = House("brick", "2000", "23")


my_prop.my_bus()
my_loc.my_crib()