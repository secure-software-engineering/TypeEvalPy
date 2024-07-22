# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (56, 97, 60)


def func2():
    return [17, 29, 79]


def func3():
    return {'nfpus': 17, 'jcwla': 86, 'hfozq': 64}


def func4():
    return 7.81


def func5():
    return 'npjtt'


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
