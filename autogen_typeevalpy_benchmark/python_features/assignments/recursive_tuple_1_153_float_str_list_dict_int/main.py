# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 97.81


def func2():
    return 'sqlcm'


def func3():
    return [5, 35, 36]


def func4():
    return {'phzbw': 98, 'jajlf': 45, 'jrnra': 4}


def func5():
    return 78


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
