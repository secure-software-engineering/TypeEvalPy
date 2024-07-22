# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14.69


def func2():
    return (62, 3, 51)


def func3():
    return {'rrujh': 63, 'matzx': 65, 'uoath': 76}


def func4():
    return 78


def func5():
    return [76, 13, 92]


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
