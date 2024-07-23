# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [50, 55, 35]


def func2():
    return 'cpulq'


def func3():
    return 47.45


def func4():
    return (38, 20, 74)


def func5():
    return {'zkcgr': 35, 'ullgi': 6, 'ynsvr': 91}


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
