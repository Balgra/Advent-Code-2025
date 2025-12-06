import file_reader

input_list=file_reader.input_reader()

dial = 50
count=0

for dial_move in input_list:
    if 'L' in dial_move:

        dial =(dial - int(dial_move.lstrip("L")) ) % 100

    if 'R' in dial_move:

        dial =(dial + int(dial_move.lstrip("R")) )% 100

    if dial == 0:
        count+=1

print(count)

# Which makes sense since we can have input as more than 3 digits, no matter the way we
# are going we require to use modulo, as we need to stay between 0 and 99.
# And for values < 100 modulo does nothing. Meanwhile it helps for values >= 100

#That's the right answer! You are one gold star closer to decorating the North Pole.