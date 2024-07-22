# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nmqei'


def func2():
    return 12.78


def func3():
    return (43, 4, 74)


def func4():
    return 50


def func5():
    return {'gplub': 50, 'mgrnc': 75, 'jhpqd': 49}


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
