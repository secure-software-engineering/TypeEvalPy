# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [81, 45, 42]


def func2():
    return 87


def func3():
    return (21, 12, 51)


def func4():
    return 68.2


def func5():
    return {'raizy': 59, 'rkdbq': 97, 'yboik': 77}


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
