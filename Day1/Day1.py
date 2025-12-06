

import file_reader

input_list=file_reader.input_reader()

#Part1

# for dial_move in input_list:
#     if 'L' in dial_move:

#         dial =(dial - int(dial_move.lstrip("L")) ) % 100

#     if 'R' in dial_move:

#         dial =(dial + int(dial_move.lstrip("R")) )% 100

#     if dial == 0:
#         count+=1

# print(count)



#Part 2

dial = 50
count=0

for dial_move in input_list:

    if 'L' in dial_move:
        dial_comp = dial - int(dial_move.lstrip("L"))

        if dial_comp < 1:
            count += ((dial-1) // 100) - ((dial_comp-1) // 100)  #trick floor function (parition coverage start 50 L100 and so on)

        dial =(dial_comp) % 100

    if 'R' in dial_move:
        dial_comp = dial + int(dial_move.lstrip("R"))

        if dial_comp>99:
            count+= dial_comp//100

        dial =dial_comp % 100


print(count)

# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 1!