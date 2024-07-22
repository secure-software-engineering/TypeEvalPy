# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'yanxu'


def func2():
    return 4


def func3():
    return (24, 26, 76)


def func4():
    return [69, 35, 94]


(a, b), (c, d) = [(func1, func2), (func3, func4)]