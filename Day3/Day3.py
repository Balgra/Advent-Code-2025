import file_reader

input_list=file_reader.input_reader()

# result =0

# for elem in input_list:
    
#     for digit in "9876543210":
        
#         if digit in elem:

#             index = elem.index(digit)     

#             tail = elem[index+1:]
            
#             if tail: # check for empty case

#                 result+= int(digit + max(tail))
#                 break
            
# print(result)



# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]



def max_k_digits_ordered(s: str) -> str:
    stack = []
    to_remove = len(s) - 12 

    for digit in s:
        while stack and to_remove > 0 and digit > stack[-1]:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return ''.join(stack[:12])

rez=0
for elem in input_list:

    rez+=int(max_k_digits_ordered(elem))
    # print(max_k_digits_ordered(elem))

print(rez)

# That's the right answer! You are one gold star closer to decorating the North Pole.

# You have completed Day 3!
