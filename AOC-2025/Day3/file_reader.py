

def input_reader():

    with open("inputs.txt") as f:
        input_list = [line.strip() for line in f]
        
    return input_list


