# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [89, 70, 57]


def func2():
    return (89, 85, 17)


def func3():
    return {'vkvsy': 94, 'htdiz': 66, 'atddy': 28}


def func4():
    return 93


(a, b), (c, d) = [(func1, func2), (func3, func4)]
