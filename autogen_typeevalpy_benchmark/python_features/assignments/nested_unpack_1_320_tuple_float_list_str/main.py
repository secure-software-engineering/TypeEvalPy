# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (62, 36, 51)


def func2():
    return 72.78


def func3():
    return [81, 74, 59]


def func4():
    return 'cykqo'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
