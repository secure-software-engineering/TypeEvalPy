# A program that defines a function called `combined_types` which performs different operations on the input value based on its type.
# The function calls different functions depending on the type of the input value.
# The behavior of the program is flow-sensitive as the functions called depend on the flow of the program execution.


def combined_types(value):
    if isinstance(value, int):
        return int_operation(value)
    elif isinstance(value, str):
        return string_operation(value)
    else:
        return None


def int_operation(x):
    return x * 2


def string_operation(s):
    return s.upper()


result1 = combined_types(5)
result2 = combined_types("hello")
result3 = combined_types(2.5)
