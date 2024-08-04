# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return {'pyhcz': 32, 'ekils': 50, 'kuiur': 54}


def func3():
    return (71, 64, 69)


def func4():
    return 'nnvkp'


def func5():
    return [54, 68, 74]


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
