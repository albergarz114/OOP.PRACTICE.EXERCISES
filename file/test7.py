class Building:
#from CHATGPT
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

# Create instances of the subclasses
my_prop = Office("cement", "1996", "27")
my_loc = House("brick", "2000", "23")

# Create dictionaries using the data from instances
office_dict = {
    "type": my_prop.type,
    "birth": my_prop.birth,
    "age": my_prop.age
}

house_dict = {
    "type": my_loc.type,
    "birth": my_loc.birth,
    "age": my_loc.age
}

# Print the dictionaries
print("Office Dictionary:", office_dict)
print("House Dictionary:", house_dict)

# Access specific values from the dictionaries
print("Type of my_prop:", office_dict["type"])
print("Age of my_loc:", house_dict["age"])
