# Two variables are assigned a value via a tuple assignment.
def func1():
    return 35.84


def func2():
    return (29, 83, 57)


def func3():
    return {'zhtta': 42, 'veslq': 50, 'apfaq': 85}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
