# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fyoac': 60, 'kxmdv': 84, 'kpozx': 58}


def func2():
    return 'tvxat'


def func3():
    return (53, 97, 36)


def func4():
    return [65, 65, 89]


def func5():
    return 24.6


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
