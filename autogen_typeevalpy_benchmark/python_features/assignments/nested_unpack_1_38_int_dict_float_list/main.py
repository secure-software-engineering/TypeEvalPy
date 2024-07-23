# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1


def func2():
    return {'kadqw': 22, 'jjbdk': 55, 'qgyxj': 47}


def func3():
    return 84.62


def func4():
    return [73, 55, 58]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
