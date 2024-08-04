# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rziaa': 77, 'bknrj': 85, 'sgaqb': 28}


def func2():
    return [77, 82, 16]


def func3():
    return (91, 16, 12)


def func4():
    return 78


(a, b), (c, d) = [(func1, func2), (func3, func4)]
