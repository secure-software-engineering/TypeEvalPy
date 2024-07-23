# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (41, 6, 49)


def func2():
    return 'kpwtq'


def func3():
    return {'netyl': 58, 'cmrpl': 83, 'egdzp': 53}


def func4():
    return 95.23


(a, b), (c, d) = [(func1, func2), (func3, func4)]
