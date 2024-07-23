# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'pzrrv'


def func2():
    return (20, 92, 70)


def func3():
    return {'iporn': 74, 'rcagy': 1, 'levao': 77}


def func4():
    return [54, 58, 79]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
