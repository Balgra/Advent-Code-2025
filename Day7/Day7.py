import math


import file_reader


matrix = file_reader.input_reader()


s_index = matrix[0].index('S')
matrix[1][s_index]='|'

counter=0
for i in range(2,len(matrix)):

    for j in range(0,len(matrix[i])):

        if matrix[i][j] == '.' and matrix[i-1][j] == '|':
            matrix[i][j] = '|'

        if matrix[i][j] == '^' and matrix[i-1][j] == '|':

            counter+=1
            matrix[i][j-1] = '|'
            matrix[i][j+1] = '|'



print(counter)

# That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]