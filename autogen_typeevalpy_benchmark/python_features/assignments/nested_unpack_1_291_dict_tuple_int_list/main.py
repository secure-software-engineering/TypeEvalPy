# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zgkuq': 84, 'mzvza': 86, 'iiskf': 67}


def func2():
    return (59, 87, 69)


def func3():
    return 20


def func4():
    return [95, 75, 30]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
