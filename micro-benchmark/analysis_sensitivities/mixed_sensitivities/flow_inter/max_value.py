# A program that defines a function called `max_value` which returns the maximum value from the input parameters.
# The function calls another function 'find_max' depending on the type of the input parameters.
# The behavior of the program is flow-sensitive as the function called depends on the flow of the program execution.


def max_value(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return find_max(a, b)
    elif isinstance(a, float) or isinstance(b, float):
        return find_max(float(a), float(b))
    else:
        return None


def find_max(x, y):
    return max(x, y)


result1 = max_value(5, 10)
result2 = max_value(3.5, 2)
result3 = max_value("Hello", "World")
