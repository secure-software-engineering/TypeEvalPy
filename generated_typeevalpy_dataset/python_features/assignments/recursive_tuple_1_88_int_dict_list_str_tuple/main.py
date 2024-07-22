# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 45


def func2():
    return {'qsxty': 31, 'ujyig': 1, 'eawws': 37}


def func3():
    return [95, 54, 33]


def func4():
    return 'rtcqj'


def func5():
    return (72, 2, 66)


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
