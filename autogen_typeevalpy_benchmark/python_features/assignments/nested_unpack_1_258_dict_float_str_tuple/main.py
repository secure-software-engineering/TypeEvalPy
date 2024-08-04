# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qwxva': 30, 'ohdxr': 54, 'cjypq': 31}


def func2():
    return 57.72


def func3():
    return 'lipld'


def func4():
    return (84, 18, 75)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
