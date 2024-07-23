# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54


def func2():
    return {'ptmfe': 49, 'dddqq': 97, 'pnkud': 69}


def func3():
    return [98, 76, 34]


def func4():
    return 'yyzej'


def func5():
    return (67, 54, 54)


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
