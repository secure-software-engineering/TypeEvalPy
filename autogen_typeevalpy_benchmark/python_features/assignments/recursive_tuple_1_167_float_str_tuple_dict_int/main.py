# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15.52


def func2():
    return 'zovwj'


def func3():
    return (53, 34, 95)


def func4():
    return {'hkyxi': 83, 'aodcg': 13, 'jmjra': 69}


def func5():
    return 6


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
