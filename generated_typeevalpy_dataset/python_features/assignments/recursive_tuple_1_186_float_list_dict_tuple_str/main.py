# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 57.27


def func2():
    return [36, 81, 41]


def func3():
    return {'snfxc': 29, 'sjdzu': 32, 'tnpfd': 91}


def func4():
    return (63, 84, 97)


def func5():
    return 'gwfdc'


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
