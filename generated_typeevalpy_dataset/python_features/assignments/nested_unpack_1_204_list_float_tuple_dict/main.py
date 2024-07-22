# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [65, 34, 50]


def func2():
    return 69.87


def func3():
    return (81, 80, 89)


def func4():
    return {'zaoxc': 9, 'hmkod': 53, 'ajqsv': 88}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
