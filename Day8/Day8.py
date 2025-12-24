
from collections import defaultdict
import file_reader
from math import prod

lines = file_reader.input_reader()

int_points=[]

for line in lines:
    x,y,z = map(int, line[0].split(','))

    # print(x,y,z)
    int_points.append((x,y,z))

# print(int_points)

distance = []

for n , (x1,y1,z1) in enumerate(int_points):
    for m , (x2,y2,z2) in enumerate(int_points):

        if n < m:
            d = pow(x1-x2,2) + pow(y1-y2,2) + pow(z1-z2,2)
            distance.append([d,n,m])

# print(distance)

root = {i : i for i in range(0,len(int_points))}

# print(root)

def find_set(v) :
    if (v == root[v]):
        return v
    root[v] = find_set(root[v])
    return root[v]



def union_sets( a,  b) :
    root[find_set(b)] = find_set(a)

wires = 1000

for d, n, m in sorted(distance)[:wires]:

    union_sets(n,m)

sizes = defaultdict(int)

for x in range(0,len(int_points)):

    sizes[find_set(x)] +=1

rez = prod(sorted(sizes.values(), reverse=True)[:3])

print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]