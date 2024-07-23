# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nvinz': 50, 'ljxzk': 5, 'glbmj': 10}


def func2():
    return 'kbzzi'


def func3():
    return [95, 55, 11]


def func4():
    return 53.55


def func5():
    return (71, 30, 35)


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
