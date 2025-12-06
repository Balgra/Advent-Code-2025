

def input_reader():

    with open("inputs.txt") as f:
        input_list = f.read().split(",")
        
    input_dict = {}
    
    for elem in input_list:
        a,b=elem.split("-")
        input_dict[int(a)] = int(b)
    return input_dict
