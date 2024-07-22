# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 53.96


def func2():
    return [30, 59, 66]


def func3():
    return {'vqldi': 52, 'hhvqf': 8, 'xkhiv': 100}


def func4():
    return 'mlttt'


def func5():
    return 73


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
