class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self): 
        print(f"woof! my name is {self.name}")