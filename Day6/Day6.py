import math


import file_reader

num_rows,operators=file_reader.input_reader()

rez=0

for nums,op in zip(zip(*num_rows), operators):

    if op == '+':
        rez +=sum(nums)
    
    if op == '*':
        rez += math.prod(nums)

print(rez)

# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]