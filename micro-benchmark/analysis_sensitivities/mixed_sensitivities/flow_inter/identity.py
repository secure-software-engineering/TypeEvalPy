# Program defines a function called 'identity' which returns the input variable as it is.
# The function calls another function 'operation' depending on type of parameter .


def identity(x):
    if isinstance(x, str):
        return string_operation(x)
    elif isinstance(x, int):
        return int_operation(x)
    else:
        return x


def string_operation(a):
    result = a + "string"
    return result


def int_operation(a):
    result = a + 1
    return result


result1 = identity(5)
result2 = identity("Hello")
