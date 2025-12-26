
import file_reader
from functools import cache


lines = file_reader.input_reader()

dict_nodes={}

# def paths(start: str, end: str) -> int:

#     if start == end :
#         return 1
    
#     return sum(paths(n, end) for n in dict_nodes[start])



# for line in lines:

#     node, *outs = line.split()

#     dict_nodes[node.strip(':')] = outs

# # print(dict_nodes)

# rez = paths('you', 'out')

# print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole.


@cache
def paths(start: str, end: str) -> int:

    if start == end :
        return 1
    
    return sum(paths(n, end) for n in dict_nodes.get(start, []))


for line in lines:

    node, *outs = line.split()

    dict_nodes[node.strip(':')] = outs

# print(dict_nodes)
#check for whether fft or dac first:

if paths('fft', 'dac'):
    
    first, second = ('fft', 'dac')
else:
   first, second = ('dac', 'fft')



rez = paths('svr', first) * paths(first, second) * paths(second, 'out')

print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 11!