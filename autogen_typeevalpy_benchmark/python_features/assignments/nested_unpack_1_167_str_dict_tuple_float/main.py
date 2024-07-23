# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'owexu'


def func2():
    return {'cptmp': 19, 'wxhql': 83, 'azvcg': 12}


def func3():
    return (79, 74, 91)


def func4():
    return 55.72


(a, b), (c, d) = [(func1, func2), (func3, func4)]
