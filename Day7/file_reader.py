


def input_reader():
    with open("inputs.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]

    return matrix
