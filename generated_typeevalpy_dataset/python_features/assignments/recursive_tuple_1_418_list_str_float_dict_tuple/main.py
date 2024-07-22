# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [70, 58, 11]


def func2():
    return 'yqeuf'


def func3():
    return 82.65


def func4():
    return {'qhopg': 58, 'hkbfs': 3, 'awfyk': 62}


def func5():
    return (49, 17, 56)


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
