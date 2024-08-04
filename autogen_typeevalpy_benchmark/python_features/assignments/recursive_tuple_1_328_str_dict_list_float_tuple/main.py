# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bylkl'


def func2():
    return {'yuhvo': 85, 'knyuq': 71, 'hpbzf': 37}


def func3():
    return [100, 15, 31]


def func4():
    return 92.64


def func5():
    return (50, 72, 93)


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
