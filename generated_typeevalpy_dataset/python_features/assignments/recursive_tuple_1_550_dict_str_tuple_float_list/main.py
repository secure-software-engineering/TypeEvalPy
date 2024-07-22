# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ndetg': 32, 'uktdg': 11, 'ytios': 6}


def func2():
    return 'dzexw'


def func3():
    return (38, 60, 5)


def func4():
    return 31.81


def func5():
    return [77, 38, 89]


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
