# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'kzgve': 57, 'bzfkq': 92, 'colpc': 34}


def func2():
    return [14, 5, 10]


def func3():
    return (10, 74, 94)


def func4():
    return 'glxdq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
