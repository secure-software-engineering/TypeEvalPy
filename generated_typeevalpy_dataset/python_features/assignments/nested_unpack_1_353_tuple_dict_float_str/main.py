# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (26, 52, 23)


def func2():
    return {'qscsm': 98, 'cpndm': 9, 'svbjk': 58}


def func3():
    return 84.73


def func4():
    return 'ayxmx'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
