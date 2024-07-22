# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 68


def func2():
    return {'vmbhc': 29, 'mtetu': 44, 'egdzm': 80}


def func3():
    return (91, 38, 31)


def func4():
    return 'jdzfl'


def func5():
    return [76, 48, 85]


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
