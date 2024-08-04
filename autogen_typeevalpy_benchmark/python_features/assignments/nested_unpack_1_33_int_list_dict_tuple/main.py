# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 87


def func2():
    return [74, 76, 3]


def func3():
    return {'zrhbt': 86, 'mqxep': 14, 'qmcji': 21}


def func4():
    return (43, 53, 89)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
