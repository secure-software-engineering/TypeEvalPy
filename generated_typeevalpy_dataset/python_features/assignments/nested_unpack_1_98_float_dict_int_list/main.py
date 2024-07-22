# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 3.22


def func2():
    return {'vatce': 78, 'jhzka': 74, 'cvjxa': 10}


def func3():
    return 62


def func4():
    return [30, 55, 25]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
