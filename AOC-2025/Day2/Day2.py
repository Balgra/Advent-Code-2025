import file_reader
# import logging

# # logging.basicConfig(filename='output.log', level=logging.INFO)

input_dict=file_reader.input_reader()
# # print(input_dict)
# # only of some sequence of digits repeated twice

# result = 0

# def check_duplicate(start,finish):
#     result=0
#     for i in range(start,finish+1):
#         i=str(i)
#         if len(i) %2 ==0:
#             l=0
#             r=len(i)//2
#             rez=0
#             while l<len(i)//2 and r<len(i):
#                 if i[l] == i[r]:
#                     rez+=1
#                 l+=1
#                 r+=1
#             if rez == len(i)//2:
#                 # logging.info(i)
#                 result+=int(i)
#             else:
#                 result+=0
#     return result
        

# for key,value in input_dict.items():

#     result+=check_duplicate(key,value)

# print(result)

# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]


#Part2

result = 0

def is_repetition(num):
    s = str(num)
    n = len(s)
    
    for size in range(1, n//2 + 1):
        if n % size == 0: 
            chunk = s[:size] # 824824824 -> 8, 82, 824
            if chunk * (n // size) == s:
                return True  
                
    return False  


def check_duplicate(start, finish):
    rez = 0
    for i in range(start, finish + 1):
        if is_repetition(i):
            rez += i
    return rez
        

for key,value in input_dict.items():

    result+=check_duplicate(key,value)

print(result)

# Both parts of this puzzle are complete! They provide two gold stars: **