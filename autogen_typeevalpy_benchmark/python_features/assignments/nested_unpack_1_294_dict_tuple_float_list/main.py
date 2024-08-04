# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qjewc': 35, 'aysph': 67, 'sumdd': 58}


def func2():
    return (53, 31, 23)


def func3():
    return 61.44


def func4():
    return [5, 77, 24]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
