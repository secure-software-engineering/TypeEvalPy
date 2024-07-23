# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 5


def func2():
    return (72, 56, 99)


def func3():
    return {'bjxgu': 11, 'bmrvz': 58, 'drqbn': 100}


def func4():
    return 'ixdef'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
