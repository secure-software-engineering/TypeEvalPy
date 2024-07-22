# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 12.0


def func2():
    return {'snzrh': 19, 'ermmc': 8, 'saxkh': 18}


def func3():
    return 51


def func4():
    return 'tkfhy'


def func5():
    return (92, 22, 28)


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
