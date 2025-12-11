


def input_reader():

    ingredient_ids = []
    ingredients=[]

    with open("inputs.txt") as f:
        for line in f:
            if '-' in line:
                ingredient_ids.append(line.strip())
            else:
                ingredients.append(line.strip())

    return (ingredient_ids,ingredients)

# print(input_reader())

