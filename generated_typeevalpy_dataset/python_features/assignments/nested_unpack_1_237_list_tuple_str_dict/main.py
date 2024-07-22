# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [81, 55, 69]


def func2():
    return (18, 31, 76)


def func3():
    return 'odtmj'


def func4():
    return {'gkddr': 36, 'vrkgy': 23, 'zztom': 21}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
