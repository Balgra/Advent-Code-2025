# import math


import file_reader


# matrix = file_reader.input_reader()


# # s_index = matrix[0].index('S')
# # matrix[1][s_index]='|'

# # counter=0
# # for i in range(2,len(matrix)):

# #     for j in range(0,len(matrix[i])):

# #         if matrix[i][j] == '.' and matrix[i-1][j] == '|':
# #             matrix[i][j] = '|'

# #         if matrix[i][j] == '^' and matrix[i-1][j] == '|':

# #             counter+=1
# #             matrix[i][j-1] = '|'
# #             matrix[i][j+1] = '|'



# # print(counter)

# # That's the right answer! You are one gold star closer to decorating the North Pole. [Continue to Part Two]

# #count how many ways you can get to a pipe

# Part2

def count_timelines(matrix):

    ways = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    start_col = matrix[0].index('S')
    ways[0][start_col] = 1

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):

            count = ways[i - 1][j]

            if matrix[i][j] == '.':
                ways[i][j] += count

            elif matrix[i][j] == '^':
                if j > 0:
                    ways[i][j - 1] += count
                if j < len(matrix[0]) - 1:
                    ways[i][j + 1] += count


    print(sum(ways[-1]))


matrix = file_reader.input_reader_part2()
count_timelines(matrix)





# That's the right answer! You are one gold star closer to decorating the North Pole.
# 48021610271997
# You have completed Day 7! You can [Share] this victory or [Return to Your Advent Calendar].