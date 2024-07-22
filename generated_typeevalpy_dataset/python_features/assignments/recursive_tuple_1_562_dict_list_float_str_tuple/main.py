# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pwgdo': 40, 'bdtwg': 32, 'xobdk': 54}


def func2():
    return [93, 60, 33]


def func3():
    return 31.17


def func4():
    return 'xpkfo'


def func5():
    return (32, 100, 85)


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
