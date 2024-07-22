# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 63.71


def func2():
    return 'eimkc'


def func3():
    return (85, 68, 72)


def func4():
    return {'znloq': 68, 'mpfhw': 72, 'rnlqq': 56}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
