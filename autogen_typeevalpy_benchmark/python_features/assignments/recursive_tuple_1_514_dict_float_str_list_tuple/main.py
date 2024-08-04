# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pponq': 8, 'nftaf': 1, 'lktts': 45}


def func2():
    return 93.69


def func3():
    return 'tofkw'


def func4():
    return [1, 42, 81]


def func5():
    return (6, 42, 23)


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
