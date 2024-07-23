# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dadev'


def func2():
    return {'fymvg': 16, 'kbnel': 43, 'jgica': 17}


def func3():
    return (48, 30, 3)


def func4():
    return [24, 41, 44]


def func5():
    return 33.56


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
