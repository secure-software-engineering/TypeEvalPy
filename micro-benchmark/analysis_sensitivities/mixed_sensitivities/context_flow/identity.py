# This program is Flow sensitive as the behavior of the program is dependent on the flow of execution, specifically the values assigned to the 'x' parameter of the 'identity' function.
# Also context sensitive as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'x' parameter of the 'identity' function.


def identity(x):
    if isinstance(x, str):
        return x.upper()
    elif isinstance(x, int):
        return x + 1
    else:
        return None


a = identity(5)
b = identity("hello")
c = identity(2.5)
