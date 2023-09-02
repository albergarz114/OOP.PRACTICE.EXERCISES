class Beer: #class attributes
    drinks = 0
    # constructor method
    def __init__(self, temperature, style, color):
        # instances/object method
        self.temperature = temperature
        self.style = style
        self.color = color
        Beer.drinks += 1

    #instance/object method
    def start(self):
        print(f"A lager beer is a {self.color} {self.style} and the temperature is {self.temperature}.")

    #instances/object method
    def stop(self):
        print(f"An ale has the color of {self.color} and served temperature is {self.temperature}.")

    @classmethod
    def get_drinksbeer(cls):
        print(f"I am done drinking at {cls.drinks} p.m.")


#create an object of the Car class

my_beer = Beer("7", "Pilsner", "Pale")
my_ale = Beer("10", "Wheat Ale", "Amber")

my_beer.start()
my_beer.stop()

my_ale.start()
my_ale.stop()

Beer.get_drinksbeer()


