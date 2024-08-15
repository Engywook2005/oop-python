from random import randint

class Apple:
    def __init__(self, field, sprite):
        self.field = field
        self.position = (0, 0)
        self.sprite = sprite
        print("init")
        print(self.position)

    def spawn(self, occupied_positions):
        while True:
            self.position = (
                randint(0, self.field[0]),
                randint(0, self.field[1]),                
            )
            if(self.position not in occupied_positions):
                break
        
        return self