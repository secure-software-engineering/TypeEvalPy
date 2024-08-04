# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 88


def func2():
    return {'vqxqi': 68, 'lptch': 65, 'tedoz': 35}


def func3():
    return [22, 33, 62]


def func4():
    return 96.77


(a, b), (c, d) = [(func1, func2), (func3, func4)]
