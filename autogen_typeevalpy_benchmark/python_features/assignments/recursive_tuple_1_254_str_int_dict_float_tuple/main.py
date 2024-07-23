# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'najyd'


def func2():
    return 54


def func3():
    return {'zspqq': 32, 'gtwut': 58, 'joxsb': 81}


def func4():
    return 4.18


def func5():
    return (4, 15, 42)


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
