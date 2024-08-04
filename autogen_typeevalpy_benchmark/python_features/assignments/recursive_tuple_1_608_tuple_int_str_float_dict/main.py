# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 73, 79)


def func2():
    return 54


def func3():
    return 'lzpbi'


def func4():
    return 54.32


def func5():
    return {'ejzny': 95, 'honur': 10, 'gbdwr': 60}


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
