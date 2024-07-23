# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (66, 63, 10)


def func2():
    return 51.24


def func3():
    return [20, 90, 37]


def func4():
    return {'lbepu': 10, 'hsxkn': 76, 'qnbaz': 26}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
