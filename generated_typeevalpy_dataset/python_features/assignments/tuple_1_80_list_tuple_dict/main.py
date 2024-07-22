# Two variables are assigned a value via a tuple assignment.
def func1():
    return [82, 7, 77]


def func2():
    return (61, 39, 24)


def func3():
    return {'rdhql': 40, 'ljoqw': 7, 'oqulm': 59}


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
