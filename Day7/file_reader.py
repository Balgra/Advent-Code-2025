


def input_reader():
    with open("inputs.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]

    return matrix

def input_reader_part2():
    with open("inputs.txt", "r") as f:
        return [list(line.rstrip("\n")) for line in f]
