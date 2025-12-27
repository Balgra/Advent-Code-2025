

def input_reader():
    with open("inputs.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    operators = lines[-1].split()

    num_rows = [list(map(int, line.split())) for line in lines[:-1]]
    
    # for nums in zip(*num_rows): #zip function takes from a list of list each element form each list(at a certain index) and puts them together
    #     print(nums)


    return num_rows,operators


#input reader for part 2
def input_reader_part2():
    with open('inputs.txt', "r") as f:
        lines = f.readlines()

    return lines
