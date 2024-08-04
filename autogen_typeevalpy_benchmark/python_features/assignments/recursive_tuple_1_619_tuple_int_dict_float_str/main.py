# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (66, 60, 91)


def func2():
    return 64


def func3():
    return {'lexlh': 25, 'gnbyu': 98, 'xvcfn': 77}


def func4():
    return 9.38


def func5():
    return 'zkaxh'


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
