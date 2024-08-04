# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72.73


def func2():
    return (16, 21, 97)


def func3():
    return 'fytjz'


def func4():
    return 54


def func5():
    return {'ezujg': 84, 'clauk': 39, 'wjyvl': 30}


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
