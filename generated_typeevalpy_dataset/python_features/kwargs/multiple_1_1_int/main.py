# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 49
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=49, b=49, c=49)
