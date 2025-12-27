
import file_reader
from functools import cache


lines = file_reader.input_reader()


*gifts_s, trees_s = lines.split("\n\n")

gifts = {}
for s in gifts_s:
    line = s.split("\n")
    gifts[int(line[0].strip(":"))] = line[1:]


rez = 0
for line in trees_s.split("\n"):

    dims_s, nums_s = line.split(": ")
    w, h = map(int, dims_s.split("x"))
    nums = list(map(int, nums_s.split(" ")))
    space = w * h
    min_space_needed = sum(c * "".join(gifts[i]).count("#") for i, c in enumerate(nums))

    if min_space_needed < space:
        rez += 1


print(rez)
