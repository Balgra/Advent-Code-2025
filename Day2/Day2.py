import file_reader
import logging

# logging.basicConfig(filename='output.log', level=logging.INFO)

input_dict=file_reader.input_reader()
# print(input_dict)
# only of some sequence of digits repeated twice

result = 0

def check_duplicate(start,finish):
    result=0
    for i in range(start,finish+1):
        i=str(i)
        if len(i) %2 ==0:
            l=0
            r=len(i)//2
            rez=0
            while l<len(i)//2 and r<len(i):
                if i[l] == i[r]:
                    rez+=1
                l+=1
                r+=1
            if rez == len(i)//2:
                # logging.info(i)
                result+=int(i)
            else:
                result+=0
    return result
        

for key,value in input_dict.items():

    result+=check_duplicate(key,value)

print(result)

# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]