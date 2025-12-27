


def input_reader():
    with open("inputs.txt", "r") as f:
        lines = list(map(str.strip, f.readlines()))

    return lines