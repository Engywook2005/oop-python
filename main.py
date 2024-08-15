from app.apple import Apple
from app.snake import Snake

# Todo move to controller class that has a loop to keep the game going.

occupied_positions = [(0,0)]

field = (11, 11)

apple = Apple(field, None)
snake = Snake(field, None)

print(tuple(snake.positions))

new_position = apple.spawn(occupied_positions).position
occupied_positions.append(new_position)

# print(new_position)
# print(occupied_positions)
