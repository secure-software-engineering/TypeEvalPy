# A Python program that defines a function called 'identity' which will simply return the variable, but also performs type checking and casting.
# The given code is flow sensitive because it produces different results based on the flow of the program execution.


def identity(x):
    if isinstance(x, str):
        return str(x)
    elif isinstance(x, int):
        return int(x)
    elif isinstance(x, float):
        return float(x)
    else:
        return x


result1 = identity(5)
result2 = identity(5.2)
result3 = identity("Hello")
result4 = identity([1, 2, 3])
