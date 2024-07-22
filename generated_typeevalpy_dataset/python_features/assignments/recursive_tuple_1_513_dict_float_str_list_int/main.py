# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mkxav': 16, 'ucywf': 79, 'wsxra': 96}


def func2():
    return 84.66


def func3():
    return 'hcfxq'


def func4():
    return [100, 41, 63]


def func5():
    return 40


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
