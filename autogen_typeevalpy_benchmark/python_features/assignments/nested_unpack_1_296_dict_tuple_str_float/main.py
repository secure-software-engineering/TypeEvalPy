# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'cnzrs': 72, 'jtilx': 91, 'ulsew': 20}


def func2():
    return (24, 38, 81)


def func3():
    return 'ddoxh'


def func4():
    return 18.46


(a, b), (c, d) = [(func1, func2), (func3, func4)]
