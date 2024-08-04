# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [64, 79, 92]


def func2():
    return 72.78


def func3():
    return {'elvwl': 63, 'eebbg': 91, 'xmnmc': 42}


def func4():
    return 'dyynd'


def func5():
    return (4, 87, 97)


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
