


import file_reader

input_matrix=file_reader.input_reader()

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

moveable_boxes = 0

for line in range(len(input_matrix)):
    for column in range(len(input_matrix[line])):

        if input_matrix[line][column] != '@': # checking only where we have papers
            continue  

        box_count = 0

        for dx, dy in dirs:
            
            nx, ny = line + dx, column + dy

            if 0 <= nx < len(input_matrix) and 0 <= ny < len(input_matrix[nx]):
                if input_matrix[nx][ny] == '@':
                    box_count += 1

        if box_count < 4:
            moveable_boxes += 1

print(moveable_boxes)



# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]
        
            



