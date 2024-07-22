# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [62, 81, 9]


def func2():
    return {'euqeu': 82, 'ysdsi': 82, 'jlkwk': 61}


def func3():
    return (69, 39, 86)


def func4():
    return 9


(a, b), (c, d) = [(func1, func2), (func3, func4)]
