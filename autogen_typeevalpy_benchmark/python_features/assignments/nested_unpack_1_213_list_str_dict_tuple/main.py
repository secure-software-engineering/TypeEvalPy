# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [93, 69, 57]


def func2():
    return 'mlcap'


def func3():
    return {'ytydb': 88, 'qexec': 46, 'yxtqv': 72}


def func4():
    return (90, 71, 16)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
