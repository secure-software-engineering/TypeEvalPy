# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'vymbw': 41, 'fvetx': 23, 'yineu': 18}


def func2():
    return 31.5


def func3():
    return [48, 93, 6]


def func4():
    return (86, 74, 69)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
