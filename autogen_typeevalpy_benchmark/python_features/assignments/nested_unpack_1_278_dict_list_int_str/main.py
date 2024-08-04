# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lfwhu': 38, 'rxysx': 8, 'zppnw': 48}


def func2():
    return [71, 7, 1]


def func3():
    return 91


def func4():
    return 'ozcha'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
