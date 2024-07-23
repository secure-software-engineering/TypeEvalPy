# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pztoc'


def func2():
    return 53


def func3():
    return (3, 12, 87)


def func4():
    return 72.31


def func5():
    return {'kpfre': 39, 'qiaeo': 16, 'ulmkq': 29}


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
