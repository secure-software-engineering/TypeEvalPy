# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'tygct': 85, 'qzaol': 62, 'amstj': 57}


def func2():
    return (75, 57, 37)


def func3():
    return 39.22


def func4():
    return [43, 17, 63]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
