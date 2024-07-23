# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 19.33


def func2():
    return [12, 37, 48]


def func3():
    return {'wyihk': 36, 'lyuir': 73, 'uoywv': 93}


def func4():
    return 'xtwhw'


def func5():
    return (26, 85, 2)


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
