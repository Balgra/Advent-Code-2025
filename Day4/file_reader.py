


def input_reader():

    matrix = []

    with open("inputs.txt") as f:
        for line in f:
            line = line.rstrip("\n")  # remove newline only
            matrix.append(list(line)) # convert row → list of chars

    return matrix

# print(input_reader())

