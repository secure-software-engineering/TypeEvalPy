# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'jcdam'


def func2():
    return {'suauq': 82, 'mhmix': 72, 'xtlmk': 79}


def func3():
    return (48, 85, 82)


def func4():
    return [19, 46, 14]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
