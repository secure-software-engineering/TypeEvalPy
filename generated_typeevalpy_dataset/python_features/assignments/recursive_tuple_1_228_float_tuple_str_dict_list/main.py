# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.65


def func2():
    return (2, 87, 15)


def func3():
    return 'tvude'


def func4():
    return {'ipqkg': 84, 'dhflq': 33, 'bmyxk': 49}


def func5():
    return [50, 6, 36]


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
