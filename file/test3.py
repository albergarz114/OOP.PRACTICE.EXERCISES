class Beverages:
    def __init__(self, style, yeast, color):
        self.style = style
        self.yeast = yeast
        self.color = color

class Lager(Beverages):

    def make_love(self):
        print(f"Drunk bro! I love {self.style} beer")

class Ale(Beverages):

    def make_fun(self):
        print("Drink booze")

my_lager = Lager("lager", "lager-yeast", "pale")
my_ale = Ale("ale", "ale-yeast", "amber")

my_lager.make_love()
my_ale.make_fun()

