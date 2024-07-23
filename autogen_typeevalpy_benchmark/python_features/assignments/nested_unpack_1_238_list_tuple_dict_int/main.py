# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [67, 70, 98]


def func2():
    return (7, 82, 79)


def func3():
    return {'huumr': 62, 'gtdol': 12, 'gyglo': 50}


def func4():
    return 41


(a, b), (c, d) = [(func1, func2), (func3, func4)]
