# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [68, 64, 81]


def func2():
    return {'qhmnn': 69, 'ndake': 6, 'vfyde': 1}


def func3():
    return (77, 86, 4)


def func4():
    return 'upcxv'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
