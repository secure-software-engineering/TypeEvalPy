# Example of a Python function that accepts a variable number of arguments.


def my_sum(a, b, *arguments):
    result = a + b
    for x in arguments:
        result += x
    return result


def func(a):
    return a([25, 70, 31], [25, 70, 31], [25, 70, 31])


b = func(my_sum)
