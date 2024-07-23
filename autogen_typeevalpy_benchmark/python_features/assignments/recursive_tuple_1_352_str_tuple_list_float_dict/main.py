# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rvuey'


def func2():
    return (20, 42, 70)


def func3():
    return [80, 51, 96]


def func4():
    return 32.69


def func5():
    return {'buwpm': 50, 'onedc': 58, 'qmeop': 32}


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
