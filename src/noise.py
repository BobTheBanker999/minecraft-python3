import random

def generate(min:int, max:int, length:int):

    retval = []

    # actually generate a list of values
    last_val = random.randint(min, max)
    retval.append(last_val)

    for i in range(length):
        new_val = random.randint(last_val-1, last_val+1)
        retval.append(new_val)
        last_val = new_val

    return retval
