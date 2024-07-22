# Two variables are assigned a value via a tuple assignment.
def func1():
    return 20.71


def func2():
    return {'ysaik': 78, 'xlwjn': 42, 'ozych': 92}


def func3():
    return (58, 29, 76)


a, b = func1, func2
f = a()
g = b()

c, d, e = func1, func2, func3

h = e()
