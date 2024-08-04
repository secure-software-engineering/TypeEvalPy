# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 44.66


def func2():
    return 'gvhgg'


def func3():
    return {'tjltd': 54, 'gtwjj': 30, 'nxqpl': 73}


def func4():
    return [17, 69, 32]


def func5():
    return (100, 53, 87)


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
