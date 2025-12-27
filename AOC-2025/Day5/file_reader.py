


def input_reader():

    ingredient_ids = []
    ingredients=[]

    with open("inputs.txt") as f:
        for line in f:
            l = line.strip()
            if not l :
                    continue
            if '-' in l:
                ingredient_ids.append(l.strip())
            else:
                ingredients.append(l.strip())

    return (ingredient_ids,ingredients)

# print(input_reader())

