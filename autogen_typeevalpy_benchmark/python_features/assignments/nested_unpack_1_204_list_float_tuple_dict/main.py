# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [74, 71, 46]


def func2():
    return 8.22


def func3():
    return (91, 41, 68)


def func4():
    return {'febnk': 97, 'ncffi': 84, 'jftnz': 2}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
