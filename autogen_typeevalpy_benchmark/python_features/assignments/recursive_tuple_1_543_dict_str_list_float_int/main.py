# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nbmol': 78, 'tzfgk': 2, 'tlvcs': 80}


def func2():
    return 'xyjnq'


def func3():
    return [54, 3, 24]


def func4():
    return 54.95


def func5():
    return 51


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
