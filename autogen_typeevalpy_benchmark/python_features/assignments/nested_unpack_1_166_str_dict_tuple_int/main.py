# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'daehn'


def func2():
    return {'hbbgm': 28, 'wlpwi': 78, 'zxomp': 77}


def func3():
    return (97, 25, 100)


def func4():
    return 78


(a, b), (c, d) = [(func1, func2), (func3, func4)]
