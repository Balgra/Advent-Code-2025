


import file_reader

input_tuple=file_reader.input_reader()



# fresh =0
# for values in input_tuple[0]:

#     left,right = values.split('-')
#     l = int(left)
#     r = int(right)

#     for i, val in enumerate(input_tuple[1]):
#         v = int(val)
#         if l < v < r:
#             fresh+=1
#             input_tuple[1][i] = 0
            
    
# print(fresh)


# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]


# Well luckily i have already split the input in the first part of the problem


# list_ids=[]
# for values in input_tuple[0]:

#     left,right = values.split('-')
#     l = int(left)
#     r = int(right)
    

intervals = []

for values in input_tuple[0]:
    left, right = values.split('-')
    intervals.append((int(left), int(right)))


intervals.sort()


merged = []

cur_start, cur_end = intervals[0]

for start, end in intervals[1:]:

    if start <= cur_end + 1:

        cur_end = max(cur_end, end)
    else:

        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end

merged.append((cur_start, cur_end))

unique_count = sum(end - start + 1 for start, end in merged)

print(unique_count)



# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 5! You can [Share] this victory or [Return to Your Advent Calendar].