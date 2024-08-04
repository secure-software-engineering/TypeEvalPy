# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'xgefp'


def func2():
    return [67, 77, 68]


def func3():
    return (26, 5, 49)


def func4():
    return {'jtcxc': 40, 'sbcyl': 22, 'hwhxf': 67}


def func5():
    return 9


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
