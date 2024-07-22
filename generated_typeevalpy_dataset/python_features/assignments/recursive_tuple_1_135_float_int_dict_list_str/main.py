# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72.54


def func2():
    return 92


def func3():
    return {'oaffy': 88, 'apypf': 58, 'catcg': 55}


def func4():
    return [92, 60, 81]


def func5():
    return 'wkorm'


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
