# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 100


def func2():
    return (45, 45, 94)


def func3():
    return {'yqdcg': 73, 'edtby': 83, 'qmopr': 82}


def func4():
    return [80, 42, 81]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
