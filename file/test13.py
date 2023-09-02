#INHERITANCE

class Base:
    def __init__(self):
        print("Base initializer")
    
    def method(self):
        print("Base method")

class A(Base):
    def __init__(self):
        print("A's initializer")
        super().__init__()
    
    def method(self):
        print("A's method")
        super().method()

class B(Base):
    def __init__(self):
        print("B's initializer")
        super().__init__()
    def method(self):
        print("B's method")
        super().method()

class C(A, B):
    def __init__(self):
        print("C's initializer")
        super().__init__()

    def method(self):
        print("C's method")
        super().method()

c = C()
c.method()


