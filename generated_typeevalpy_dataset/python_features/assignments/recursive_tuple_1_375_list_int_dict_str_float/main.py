# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [17, 83, 3]


def func2():
    return 15


def func3():
    return {'kqmwt': 11, 'wvamo': 2, 'tcdli': 3}


def func4():
    return 'oyddi'


def func5():
    return 87.32


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
