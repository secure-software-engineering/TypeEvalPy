# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 43.67


def func2():
    return (72, 72, 66)


def func3():
    return {'kajcp': 49, 'ikhkc': 22, 'xxzoe': 18}


def func4():
    return [35, 39, 35]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
