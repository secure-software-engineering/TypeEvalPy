# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (65, 9, 46)


def func2():
    return [54, 78, 94]


def func3():
    return {'vtlab': 99, 'qqudk': 84, 'qicen': 98}


def func4():
    return 17


(a, b), (c, d) = [(func1, func2), (func3, func4)]
