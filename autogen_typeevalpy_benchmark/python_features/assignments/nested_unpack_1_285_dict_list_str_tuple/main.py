# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rquyb': 45, 'fgups': 73, 'nmzxz': 65}


def func2():
    return [12, 23, 10]


def func3():
    return 'wuual'


def func4():
    return (90, 40, 86)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
