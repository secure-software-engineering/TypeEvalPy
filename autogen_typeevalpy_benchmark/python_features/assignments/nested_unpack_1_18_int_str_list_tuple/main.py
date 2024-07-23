# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 22


def func2():
    return 'nlfey'


def func3():
    return [84, 25, 74]


def func4():
    return (87, 26, 85)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
