
from collections import defaultdict
import file_reader
from math import prod

lines = file_reader.input_reader()

int_points=[]

for line in lines:
    x,y = map(int, line.split(','))

    int_points.append((x,y))

rez = 0

for i , (x1,y1) in enumerate(int_points):
    for j , (x2,y2) in enumerate(int_points):

        if i < j:
            area = (abs(x1-x2) + 1) * (abs(y1-y2) +1)

            rez = max(rez,area)

print(rez)

#hat's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]


