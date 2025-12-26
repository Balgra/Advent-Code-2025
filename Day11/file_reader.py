


def input_reader():
    with open("inputs.txt", "r") as f:
        line = list(map(str.strip, f.readlines()))

    return line