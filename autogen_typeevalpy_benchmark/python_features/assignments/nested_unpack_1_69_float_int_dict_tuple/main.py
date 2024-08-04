# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 81.87


def func2():
    return 78


def func3():
    return {'dgqwo': 29, 'cvwht': 58, 'hxdly': 45}


def func4():
    return (4, 54, 7)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
