# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 5
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=5, b=5, c=5)
