# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [98, 53, 66]


def func2():
    return 'qmnxi'


def func3():
    return {'extti': 87, 'naver': 51, 'qdxck': 48}


def func4():
    return 38.58


def func5():
    return (77, 85, 4)


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
