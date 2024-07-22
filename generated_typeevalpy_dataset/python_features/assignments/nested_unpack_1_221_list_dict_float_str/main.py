# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [70, 8, 79]


def func2():
    return {'klcow': 2, 'ewhld': 75, 'ndgef': 91}


def func3():
    return 1.74


def func4():
    return 'nnxdd'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
