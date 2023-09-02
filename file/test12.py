class IT:
    def __init__(self, title, education):
        self.title = title
        self.education = education

class Programming(IT):
    def my_comp(self):
        print(f"I love to program and my education is in {self.education}")

class IT_Support(IT):
    def my_sys(self):
        print(f"I enjoy it a lot my title which is {self.title}")

my_comp2 = Programming("Backend Developer", "bachelors of applied technology")

my_comp3 = IT_Support("IT Administrator", "Masters of Computer Science")

my_comp2.my_comp()
my_comp3.my_sys()