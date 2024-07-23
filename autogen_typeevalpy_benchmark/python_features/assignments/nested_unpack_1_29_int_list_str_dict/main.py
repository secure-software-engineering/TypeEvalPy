# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48


def func2():
    return [17, 4, 69]


def func3():
    return 'xzuxt'


def func4():
    return {'bewyr': 35, 'xdegd': 58, 'ieexo': 65}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
