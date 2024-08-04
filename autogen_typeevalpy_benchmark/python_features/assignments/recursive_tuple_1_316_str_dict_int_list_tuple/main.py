# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mkqlp'


def func2():
    return {'jnmyw': 28, 'mjfxe': 81, 'zdsha': 67}


def func3():
    return 48


def func4():
    return [4, 58, 52]


def func5():
    return (43, 79, 59)


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
