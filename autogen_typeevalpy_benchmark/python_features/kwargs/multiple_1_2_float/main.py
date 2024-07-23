# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 2.71
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=2.71, b=2.71, c=2.71)
