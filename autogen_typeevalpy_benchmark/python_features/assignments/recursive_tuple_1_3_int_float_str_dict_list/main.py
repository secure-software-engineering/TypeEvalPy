# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 84


def func2():
    return 36.41


def func3():
    return 'scznb'


def func4():
    return {'pgvla': 100, 'xyusa': 24, 'hxoou': 95}


def func5():
    return [17, 82, 72]


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
