# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zgzik': 27, 'camwx': 54, 'bmyoy': 92}


def func2():
    return (14, 18, 49)


def func3():
    return [22, 96, 8]


def func4():
    return 40.3


def func5():
    return 'xygja'


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
