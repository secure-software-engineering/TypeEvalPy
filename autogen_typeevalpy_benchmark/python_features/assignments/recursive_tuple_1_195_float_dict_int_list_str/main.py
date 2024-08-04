# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82.31


def func2():
    return {'ayker': 50, 'vmcrc': 88, 'wuaio': 59}


def func3():
    return 2


def func4():
    return [63, 84, 86]


def func5():
    return 'kuhgq'


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
