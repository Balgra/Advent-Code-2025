


import file_reader

input_tuple=file_reader.input_reader()



fresh =0
for values in input_tuple[0]:

    left,right = values.split('-')
    l = int(left)
    r = int(right)

    for i, val in enumerate(input_tuple[1]):
        v = int(val)
        if l < v < r:
            fresh+=1
            input_tuple[1][i] = 0
            
    
print(fresh)


# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]


