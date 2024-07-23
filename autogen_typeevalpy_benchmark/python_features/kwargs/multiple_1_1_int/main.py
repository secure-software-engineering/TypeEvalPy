# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 30
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=30, b=30, c=30)
