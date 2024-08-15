RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, -1)

class Snake:
    def __init__(self, field, sprite, length = 2):
        self.field = field
        self.sprite = sprite
        self.length = length
        self.direction = RIGHT
        self.positions = self.set_initial_positions()

    def set_initial_positions(self):
        x_values = []
        y_values = []

        current_x = self.length if self.direction[0] == 1 else self.field[0] - self.length
        current_y = self.length if self.direction[1] == 1 else self.field[1] - self.length

        step_x = self.direction[0]
        step_y = self.direction[1]

        n = 0

        while n < self.length:
            current_x = current_x - step_x
            current_y = current_y - step_y

            x_values.append(current_x)
            y_values.append(current_y)

            n += 1

        return list(zip(tuple(x_values), tuple(y_values)))
