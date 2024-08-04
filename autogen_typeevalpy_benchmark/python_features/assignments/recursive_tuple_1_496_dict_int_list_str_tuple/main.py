# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qwpyc': 39, 'ezztl': 67, 'bewtm': 45}


def func2():
    return 25


def func3():
    return [37, 81, 91]


def func4():
    return 'ujmpw'


def func5():
    return (17, 5, 32)


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
