# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'unkkq': 31, 'ozjiv': 23, 'puluo': 85}


def func2():
    return 'rtsvc'


def func3():
    return (77, 60, 42)


def func4():
    return [72, 13, 57]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
