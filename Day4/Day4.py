


import file_reader

input_matrix=file_reader.input_reader()

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]



def check_papers(values_to_hold):

    moveable_boxes=0
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
                values_to_hold.append((line,column))
    return moveable_boxes


# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]

values_to_hold= []

returned_boxes = check_papers(values_to_hold)
count=0

while returned_boxes != 0:
    

    for tupples in values_to_hold:
        input_matrix[tupples[0]][tupples[1]]= '.'
        count+=1


    values_to_hold=[]

    returned_boxes = check_papers(values_to_hold)

print(count)

  
            



# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 4! You can [Shareon Bluesky Twitter Mastodon] this victory or [Return to Your Advent Calendar].