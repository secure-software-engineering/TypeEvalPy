# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hicev'


def func2():
    return [26, 62, 63]


def func3():
    return 25.66


def func4():
    return {'ktrej': 17, 'hfwpm': 95, 'svyde': 78}


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
