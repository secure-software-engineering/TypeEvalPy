# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [4, 73, 54]


def func2():
    return 'kbtmx'


def func3():
    return {'tudgn': 35, 'tqoys': 53, 'wmocc': 67}


def func4():
    return (14, 29, 42)


def func5():
    return 62.63


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
