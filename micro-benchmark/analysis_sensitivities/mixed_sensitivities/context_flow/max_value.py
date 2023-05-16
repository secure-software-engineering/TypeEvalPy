# A program that defines a function called 'max_value' which returns the maximum value between two numbers.
# The behavior of the program is flow-sensitive as it produces different results based on the flow of execution.


def max_value(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    else:
        return None


result1 = max_value(5, 10)
result2 = max_value(3.5, 2.8)
result3 = max_value(5, 3.5)
result4 = max_value("Hello", "World")
