# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [63, 11, 36]


def func2():
    return 33.67


def func3():
    return {'woqfa': 2, 'fmmme': 15, 'egcye': 97}


def func4():
    return 15


(a, b), (c, d) = [(func1, func2), (func3, func4)]
