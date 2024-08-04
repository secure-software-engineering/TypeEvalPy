# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'koknz'


def func2():
    return {'yjpst': 78, 'tnknm': 53, 'ufpjh': 49}


def func3():
    return 49


def func4():
    return 30.65


def func5():
    return (4, 41, 63)


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
