# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 3


def func2():
    return [24, 10, 97]


def func3():
    return 'fghfw'


def func4():
    return {'yvulq': 87, 'fdffm': 6, 'xcyme': 25}


def func5():
    return (82, 36, 86)


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
