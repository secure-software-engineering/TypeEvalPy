# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [29, 36, 95]


def func2():
    return (28, 77, 87)


def func3():
    return {'avxbt': 43, 'yqhyt': 78, 'gtxog': 13}


def func4():
    return 1.89


(a, b), (c, d) = [(func1, func2), (func3, func4)]
