# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qzdys': 81, 'sneox': 47, 'xiroq': 56}


def func2():
    return [95, 58, 85]


def func3():
    return 67


def func4():
    return 'cqcdy'


def func5():
    return 2.94


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
