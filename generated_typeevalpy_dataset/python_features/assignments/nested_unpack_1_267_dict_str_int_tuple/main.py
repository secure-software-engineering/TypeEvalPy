# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wxgfs': 38, 'jqnau': 9, 'ggzbk': 53}


def func2():
    return 'nmyhq'


def func3():
    return 10


def func4():
    return (12, 60, 79)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
