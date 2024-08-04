# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90


def func2():
    return [3, 51, 72]


def func3():
    return (69, 68, 63)


def func4():
    return {'bvovq': 74, 'tfrdw': 27, 'salib': 84}


def func5():
    return 16.96


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
