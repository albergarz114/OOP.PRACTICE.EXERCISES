class Feline:
    def __init__(self, breed, name, age, nationality):
        self.breed = breed
        self.name = name
        self.age = age
        self.nationality = nationality

class Cat(Feline):
    def my_cat(self):
        print(f"Hi I am the cat and my name is {self.name}")

class Lion(Feline):
    def my_calico(self):
        print(f"I am the king of the universe. My age is {self.age}")

my_tabby = Cat("short hair", "Cookies", "4", "Canadian")
my_lynx = Lion("King", "leo", "7", "Australian")

my_tabby.my_cat()
my_lynx.my_calico()