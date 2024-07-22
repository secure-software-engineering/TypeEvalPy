# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (73, 85, 40)


def func2():
    return 'xjddk'


def func3():
    return {'qgzdf': 28, 'xdpss': 98, 'mvzwf': 5}


def func4():
    return 70.85


(a, b), (c, d) = [(func1, func2), (func3, func4)]
