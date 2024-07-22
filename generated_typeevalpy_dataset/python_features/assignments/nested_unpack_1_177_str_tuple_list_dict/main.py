# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'exfhx'


def func2():
    return (59, 84, 76)


def func3():
    return [3, 16, 89]


def func4():
    return {'nqlyy': 17, 'tudfa': 79, 'djjab': 60}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
