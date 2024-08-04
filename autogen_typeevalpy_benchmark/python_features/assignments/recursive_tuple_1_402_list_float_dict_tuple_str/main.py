# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [24, 31, 82]


def func2():
    return 53.96


def func3():
    return {'yuxuv': 45, 'bazgk': 21, 'couil': 27}


def func4():
    return (94, 74, 12)


def func5():
    return 'adpus'


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
