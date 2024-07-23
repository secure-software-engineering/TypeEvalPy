# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56.88


def func2():
    return {'jnhhw': 100, 'cvdlv': 42, 'zsrif': 8}


def func3():
    return [87, 30, 88]


def func4():
    return 4


def func5():
    return (14, 49, 6)


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
