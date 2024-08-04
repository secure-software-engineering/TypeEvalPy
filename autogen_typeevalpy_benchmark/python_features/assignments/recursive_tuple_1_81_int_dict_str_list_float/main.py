# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return {'ktxef': 65, 'mrgko': 93, 'usitw': 95}


def func3():
    return 'vkcca'


def func4():
    return [20, 45, 65]


def func5():
    return 2.35


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
