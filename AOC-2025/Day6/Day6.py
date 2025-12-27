import math


import file_reader

# num_rows,operators=file_reader.input_reader()

# # rez=0

# for nums,op in zip(zip(*num_rows), operators):

#     if op == '+':
#         rez +=sum(nums)
    
#     if op == '*':
#         rez += math.prod(nums)

# print(rez)

# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]


lines = file_reader.input_reader_part2()

rez = 0
nums = []
op = ""
for val in zip(*lines):
    if all(c in " \n" for c in val):
        if op == "+":
            rez += sum(nums)
        elif op == "*":
            rez += math.prod(nums)
        
        nums = []
        op = ""
        continue
    if val[-1] in "*+":
        op = val[-1]
    nums.append(int("".join(val[:-1])))


print(rez)


# That's the right answer! You are one gold star closer to decorating the North Pole.