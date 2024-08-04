# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [38, 82, 19]


def func2():
    return 'hxzwq'


def func3():
    return 95.78


def func4():
    return (2, 71, 72)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
