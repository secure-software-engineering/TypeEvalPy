# This program is Flow sensitive as the behavior of the program is dependent on the flow of execution, specifically the values assigned to the 'x' parameter of the 'identity' function.
# Also context sensitive as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'x' parameter of the 'identity' function.


def identity(x):
    value = None
    if isinstance(x, str):
        value = x * 2
    elif isinstance(x, int):
        value = x + 1

    return value


result = identity(5)
result = identity("hello")
result = identity(2.5)
