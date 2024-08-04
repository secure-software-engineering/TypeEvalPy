# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 46.11
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=46.11, b=46.11, c=46.11)
