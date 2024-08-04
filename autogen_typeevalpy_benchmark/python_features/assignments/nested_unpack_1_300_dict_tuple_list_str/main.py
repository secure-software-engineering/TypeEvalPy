# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zarel': 1, 'opzmd': 81, 'sewqs': 10}


def func2():
    return (50, 89, 43)


def func3():
    return [68, 5, 38]


def func4():
    return 'lhyou'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
