# Defines a recursive function
def recursive_func(x):
    if x < 1:
        return x
    return x * recursive_func(x - 1)


a = recursive_func(70)
