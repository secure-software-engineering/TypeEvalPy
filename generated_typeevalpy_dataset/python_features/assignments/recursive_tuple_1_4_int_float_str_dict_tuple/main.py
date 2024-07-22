# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90


def func2():
    return 9.46


def func3():
    return 'junmw'


def func4():
    return {'kuiyt': 14, 'otaze': 69, 'qxase': 60}


def func5():
    return (31, 41, 98)


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
