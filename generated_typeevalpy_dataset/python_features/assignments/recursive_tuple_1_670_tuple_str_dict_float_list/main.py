# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (49, 84, 74)


def func2():
    return 'afaco'


def func3():
    return {'dtzsg': 59, 'yjcti': 40, 'bqept': 61}


def func4():
    return 82.07


def func5():
    return [98, 61, 94]


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
