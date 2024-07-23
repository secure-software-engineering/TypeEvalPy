# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 72.23


def func2():
    return (87, 37, 52)


def func3():
    return [85, 33, 52]


def func4():
    return {'tpqta': 21, 'otais': 96, 'rxgwm': 67}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
