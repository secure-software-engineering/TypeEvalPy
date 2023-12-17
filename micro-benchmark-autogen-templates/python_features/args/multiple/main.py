# Example of a Python function that accepts a variable number of arguments.


def my_sum(a, b, *integers):
    result = a + b
    for x in integers:
        result += x
    return result


def func(a):
    return a(1, 2, 3)


b = func(my_sum)
