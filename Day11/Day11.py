
import file_reader


lines = file_reader.input_reader()

dict_nodes={}

def paths(start: str, end: str) -> int:

    if start == end :
        return 1
    
    return sum(paths(n, end) for n in dict_nodes[start])



for line in lines:

    node, *outs = line.split()

    dict_nodes[node.strip(':')] = outs

# print(dict_nodes)

rez = paths('you', 'out')

print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole.

