# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 63, 50)


def func2():
    return 99.78


def func3():
    return 'dkgso'


def func4():
    return [1, 47, 30]


def func5():
    return {'zdjth': 6, 'dmolf': 51, 'kkivk': 51}


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
