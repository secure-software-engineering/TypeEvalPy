# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 78


def func2():
    return [100, 41, 39]


def func3():
    return 50.01


def func4():
    return {'ljzqv': 34, 'tbgbg': 10, 'gvrsg': 89}


def func5():
    return 'dnstk'


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
