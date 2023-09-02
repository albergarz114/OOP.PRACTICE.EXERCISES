class Human:
    # class attributes

    # constructor method
    def __init__(self, age, nationality, race, gender, ethnicity, name):
        #instances/object attributes
        self.age = age
        self.nationality = nationality
        self.race = race
        self.gender = gender
        self.name = name
        self.ethnicity = ethnicity


    #instances/object method
    def albert(self):
        print(f"Hello my name is {self.name} and I am {self.nationality}")
    # instances/object method
    def garza(self):
        print(f"My age is {self.age} and a {self.gender} and my race is {self.race} and my ethnicity is {self.ethnicity}")

#create an object of the Human class

my_identity = Human("33", "US-American", "White/Caucasian", "Male", "Hispanic/Latino", "Albi")  #FYI has to be the same order as the constructor method 

my_identity.albert()
my_identity.garza()