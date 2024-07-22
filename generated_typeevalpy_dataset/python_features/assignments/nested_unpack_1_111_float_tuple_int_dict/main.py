# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 19.84


def func2():
    return (34, 14, 13)


def func3():
    return 34


def func4():
    return {'uoljx': 53, 'jqhff': 99, 'ubsoh': 9}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
