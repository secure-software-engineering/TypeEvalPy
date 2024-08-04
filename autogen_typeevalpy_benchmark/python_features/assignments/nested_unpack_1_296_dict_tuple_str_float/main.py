# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rbqhl': 31, 'iutbt': 93, 'yeumd': 57}


def func2():
    return (76, 75, 42)


def func3():
    return 'ktxfc'


def func4():
    return 23.55


(a, b), (c, d) = [(func1, func2), (func3, func4)]
