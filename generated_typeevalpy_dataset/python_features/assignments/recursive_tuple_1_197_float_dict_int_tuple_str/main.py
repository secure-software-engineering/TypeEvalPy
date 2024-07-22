# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50.84


def func2():
    return {'arasu': 13, 'vjyym': 78, 'feesm': 19}


def func3():
    return 40


def func4():
    return (16, 91, 87)


def func5():
    return 'pwubb'


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
