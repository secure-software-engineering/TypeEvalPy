# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [36, 88, 40]


def func2():
    return 'wxibs'


def func3():
    return {'cwtjf': 99, 'tnyeh': 47, 'ogrct': 68}


def func4():
    return (15, 46, 76)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
