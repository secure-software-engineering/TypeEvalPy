# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [4, 5, 96]


def func2():
    return (72, 76, 46)


def func3():
    return 'fhgbt'


def func4():
    return {'yease': 79, 'bfmiy': 73, 'zjoom': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
