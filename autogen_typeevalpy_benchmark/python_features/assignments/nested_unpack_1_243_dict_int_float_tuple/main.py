# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'okoht': 58, 'pcrcf': 35, 'ekcao': 96}


def func2():
    return 73


def func3():
    return 4.32


def func4():
    return (53, 39, 12)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
