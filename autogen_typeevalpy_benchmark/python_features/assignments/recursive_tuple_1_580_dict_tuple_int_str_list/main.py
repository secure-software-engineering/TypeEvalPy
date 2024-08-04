# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'eclpf': 35, 'weaek': 24, 'yoocz': 87}


def func2():
    return (51, 35, 64)


def func3():
    return 10


def func4():
    return 'bowlw'


def func5():
    return [98, 3, 28]


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
