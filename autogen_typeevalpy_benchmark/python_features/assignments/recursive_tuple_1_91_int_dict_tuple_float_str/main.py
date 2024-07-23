# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 68


def func2():
    return {'luxyr': 3, 'fzpcj': 52, 'ewjcs': 90}


def func3():
    return (55, 39, 21)


def func4():
    return 27.69


def func5():
    return 'ywyen'


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
