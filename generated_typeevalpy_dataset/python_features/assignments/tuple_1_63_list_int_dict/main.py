# Two variables are assigned a value via a tuple assignment.
def func1():
    return [100, 41, 64]


def func2():
    return 88


def func3():
    return {'otbgs': 99, 'emrfj': 70, 'nyqzc': 49}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
