
from collections import defaultdict
import file_reader
from math import prod
from functools import cache

lines = file_reader.input_reader()

int_points=[]

for line in lines:
    x,y = map(int, line.split(','))

    int_points.append((x,y))

# rez = 0

# for i , (x1,y1) in enumerate(int_points):
#     for j , (x2,y2) in enumerate(int_points):

#         if i < j:
#             area = (abs(x1-x2) + 1) * (abs(y1-y2) +1)

#             rez = max(rez,area)

# print(rez)

#hat's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]



#ray finding
#checking if a point is within the map that we need
@cache #if solved once store it here 
def points_in_map (x: int, y: int) -> bool:

    inside_map = False

    for (x1,y1), (x2,y2) in zip(int_points, int_points[1:] + int_points[:1]):

        # assert (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) 

        if (x == x1 == x2 and min(y1, y2) <= y <= max(y1, y2) or
            y == y1 == y2 and min(x1, x2) <= x <= max(x1, x2)) : 

            return True
        
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1) :

            inside_map = not inside_map 

    return inside_map


def edge_not_intersect(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    """
    x1, y1, x2, y2 are edge to check
    rx1, ry1, rx2, ry2 are rectangle
    """
    if y1 == y2:
        if ry1 < y1 < ry2:
            if max(x1, x2) > rx1 and min(x1, x2) < rx2:
                return True
    else:
        if rx1 < x1 < rx2:
            if max(y1, y2) > ry1 and min(y1, y2) < ry2:
                return True
    return False




def valid_square(x1: int, x2: int, y1:int, y2: int):

    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])

    for x, y  in[(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if not points_in_map(x,y):
                return False
    
    for (ex1, ey1), (ex2, ey2) in zip(int_points, int_points[1:] + int_points[:1]):
        if edge_not_intersect (ex1, ey1, ex2, ey2, x1, y1, x2, y2) :
            return False

    return True
            

rez = 0

for i , (x1,y1) in enumerate(int_points):
    for j , (x2,y2) in enumerate(int_points):

        if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area > rez and valid_square(x1, x2, y1, y2):
                rez = area

print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 9!