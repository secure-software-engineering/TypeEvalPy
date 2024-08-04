# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'igcup': 44, 'wybjo': 65, 'nxerq': 9}


def func2():
    return 24


def func3():
    return (20, 41, 77)


def func4():
    return [6, 75, 89]


def func5():
    return 'iknsx'


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
