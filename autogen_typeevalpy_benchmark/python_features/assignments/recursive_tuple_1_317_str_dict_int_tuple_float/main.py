# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kmjcj'


def func2():
    return {'hxdmd': 44, 'afttp': 38, 'fkvpu': 92}


def func3():
    return 56


def func4():
    return (12, 55, 42)


def func5():
    return 75.85


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
