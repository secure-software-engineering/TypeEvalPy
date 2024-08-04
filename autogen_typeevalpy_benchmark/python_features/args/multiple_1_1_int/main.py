# Example of a Python function that accepts a variable number of arguments.


def my_sum(a, b, *arguments):
    result = a + b
    for x in arguments:
        result += x
    return result


def func(a):
    return a(83, 83, 83)


b = func(my_sum)
