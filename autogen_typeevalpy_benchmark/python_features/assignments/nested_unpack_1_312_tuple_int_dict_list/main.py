# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (8, 86, 47)


def func2():
    return 51


def func3():
    return {'dwjjh': 55, 'jzwcs': 94, 'lzuhu': 54}


def func4():
    return [18, 76, 77]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
