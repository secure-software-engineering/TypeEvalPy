# Program defines a function called 'identity' which returns the input variable as it is.
# The function calls another function 'operation' depending on type of parameter .


def identity(x):
    if isinstance(x, str):
        return identity_2(x)
    elif isinstance(x, int):
        return identity_2(x)
    else:
        return x


def identity_2(y):
    return y


result = identity(5)
result = identity(5.0)
result = identity("Hello")
