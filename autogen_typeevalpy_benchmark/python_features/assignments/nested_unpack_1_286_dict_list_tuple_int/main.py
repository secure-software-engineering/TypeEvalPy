# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wokmh': 51, 'adhfd': 83, 'sptof': 35}


def func2():
    return [91, 100, 64]


def func3():
    return (37, 56, 94)


def func4():
    return 55


(a, b), (c, d) = [(func1, func2), (func3, func4)]
