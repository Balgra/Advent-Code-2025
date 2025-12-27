


def input_reader():
    with open("inputs.txt", "r") as f:
        line = [[line.strip()] for line in f]

    return line