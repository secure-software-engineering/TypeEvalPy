# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kwfms'


def func2():
    return {'gvrjw': 17, 'obdfp': 76, 'ougxy': 12}


def func3():
    return 38.67


def func4():
    return (94, 25, 1)


def func5():
    return 78


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
