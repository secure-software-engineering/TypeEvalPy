# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 94.68
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=94.68, b=94.68, c=94.68)
