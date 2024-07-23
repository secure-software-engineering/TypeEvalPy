# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (86, 50, 40)


def func2():
    return 'yoehe'


def func3():
    return 55


def func4():
    return [5, 96, 62]


def func5():
    return {'uoaqw': 58, 'vyizk': 67, 'bsdts': 85}


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
