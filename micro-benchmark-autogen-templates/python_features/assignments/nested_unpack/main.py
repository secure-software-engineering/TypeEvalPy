# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return <value1>


def func2():
    return <value2>


def func3():
    return <value3>


def func4():
    return <value4>


(a, b), (c, d) = [(func1, func2), (func3, func4)]
a(); b(); c(); d();
