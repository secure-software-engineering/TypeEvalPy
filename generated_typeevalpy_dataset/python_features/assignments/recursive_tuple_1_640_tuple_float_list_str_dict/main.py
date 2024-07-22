# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (49, 5, 89)


def func2():
    return 44.05


def func3():
    return [17, 52, 40]


def func4():
    return 'kfium'


def func5():
    return {'qjquz': 37, 'ybmit': 98, 'vcpur': 79}


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
