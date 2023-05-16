# A program that defines a function called 'max_value' which returns the maximum value between two numbers.
# The behavior of the program is interprocedural as it involves calling a separate function ('maximum') to compute the maximum value.
# The program is also context-sensitive as the behavior of the 'maximum' function depends on the types of the inputs.


def max_value(a, b):
    result = maximum(a, b)
    return result


def maximum(a, b):
    return max(a, b)


result1 = max_value(5, 10)
result4 = max_value("Hello", "World")
