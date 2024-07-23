# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ohlmm'


def func2():
    return 17


def func3():
    return (72, 30, 68)


def func4():
    return {'dzmvl': 65, 'vzlps': 54, 'gdtrj': 75}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
