# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ovcwx': 56, 'lzkba': 16, 'pvphf': 13}


def func2():
    return [93, 32, 58]


def func3():
    return 11


def func4():
    return 'ynccp'


def func5():
    return 64.93


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
