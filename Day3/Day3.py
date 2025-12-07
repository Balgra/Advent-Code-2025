import file_reader

input_list=file_reader.input_reader()

result =0

for elem in input_list:
    
    for digit in "9876543210":
        
        if digit in elem:

            index = elem.index(digit)     

            tail = elem[index+1:]
            
            if tail: # check for empty case

                result+= int(digit + max(tail))
                break
            
print(result)



# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]