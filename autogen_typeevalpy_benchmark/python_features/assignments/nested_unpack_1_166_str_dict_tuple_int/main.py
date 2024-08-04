# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mcxsn'


def func2():
    return {'xurqd': 81, 'tezzv': 19, 'dlzlz': 77}


def func3():
    return (34, 41, 94)


def func4():
    return 9


(a, b), (c, d) = [(func1, func2), (func3, func4)]
