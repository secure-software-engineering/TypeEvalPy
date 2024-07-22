# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 76.08


def func2():
    return {'gpjgf': 96, 'xpspl': 18, 'uhlxh': 84}


def func3():
    return 'icqyn'


def func4():
    return (52, 98, 7)


def func5():
    return [58, 63, 7]


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
