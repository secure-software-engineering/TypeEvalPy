# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 61


def func2():
    return 'rzywf'


def func3():
    return {'sfgpo': 4, 'mvicv': 48, 'lyklw': 18}


def func4():
    return 58.17


def func5():
    return (17, 40, 95)


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
