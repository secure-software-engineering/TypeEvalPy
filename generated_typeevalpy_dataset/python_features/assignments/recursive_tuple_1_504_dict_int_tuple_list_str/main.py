# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'utslh': 73, 'ynyct': 68, 'ositn': 72}


def func2():
    return 15


def func3():
    return (69, 63, 76)


def func4():
    return [1, 45, 24]


def func5():
    return 'pmvtf'


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
