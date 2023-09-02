class Wood:
    def __init__(self, type, age):
        self.type = type
        self.age = age

class cherry(Wood):
    def red_cherry(self):
        print(f"I did not know there was cherry wood. It's age is {self.age} ")

class pear(Wood):
    def green_pear(self):
        print(f"It is expensive and its type is {self.type}")

my_branch = cherry("cherry", "50")
my_leaf = pear("pear", "100")

my_branch.red_cherry()
my_leaf.green_pear()