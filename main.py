from app.apple import Apple

occupied_positions = []

field = (11, 11)

apple = Apple((field), None)

new_position = apple.spawn(occupied_positions).position

print(new_position)
