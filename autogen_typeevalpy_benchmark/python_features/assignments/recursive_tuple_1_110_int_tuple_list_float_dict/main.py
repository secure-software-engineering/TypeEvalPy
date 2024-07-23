# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 62


def func2():
    return (80, 34, 6)


def func3():
    return [83, 73, 30]


def func4():
    return 5.54


def func5():
    return {'zzwcj': 81, 'pcgkj': 48, 'lgpsf': 72}


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
