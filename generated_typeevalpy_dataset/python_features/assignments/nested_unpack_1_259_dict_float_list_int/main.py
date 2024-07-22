# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'iggje': 76, 'nmzhh': 74, 'udmmi': 94}


def func2():
    return 58.27


def func3():
    return [38, 32, 30]


def func4():
    return 58


(a, b), (c, d) = [(func1, func2), (func3, func4)]
