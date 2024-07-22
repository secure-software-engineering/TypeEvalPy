# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jabyc': 55, 'nglyu': 28, 'jfhlt': 63}


def func2():
    return (88, 24, 11)


def func3():
    return 92.59


def func4():
    return 49


(a, b), (c, d) = [(func1, func2), (func3, func4)]
