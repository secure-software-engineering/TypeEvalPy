# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a="Hello", b="World", c="!")
