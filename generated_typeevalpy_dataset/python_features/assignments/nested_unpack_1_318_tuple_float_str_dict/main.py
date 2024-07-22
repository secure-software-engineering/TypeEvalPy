# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (78, 83, 74)


def func2():
    return 17.76


def func3():
    return 'cizkn'


def func4():
    return {'wrdlf': 63, 'srwje': 5, 'vbrst': 51}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
