# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [39, 16, 79]


def func2():
    return 42


def func3():
    return 'jmdll'


def func4():
    return (30, 90, 44)


def func5():
    return {'jolvq': 46, 'pthac': 86, 'kpcve': 30}


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
