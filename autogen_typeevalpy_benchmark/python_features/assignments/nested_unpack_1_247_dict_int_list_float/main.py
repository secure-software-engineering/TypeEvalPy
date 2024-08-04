# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rbyea': 92, 'ceaqk': 10, 'mqpbf': 2}


def func2():
    return 27


def func3():
    return [84, 63, 11]


def func4():
    return 47.34


(a, b), (c, d) = [(func1, func2), (func3, func4)]
