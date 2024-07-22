# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (22, 30, 80)


def func2():
    return 28


def func3():
    return [62, 27, 77]


def func4():
    return {'rjbuw': 63, 'osfsr': 77, 'ibepf': 17}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
