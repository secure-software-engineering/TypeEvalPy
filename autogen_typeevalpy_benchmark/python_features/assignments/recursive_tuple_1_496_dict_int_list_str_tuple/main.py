# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lsjpf': 67, 'dzzuu': 79, 'cshbq': 35}


def func2():
    return 93


def func3():
    return [61, 59, 42]


def func4():
    return 'cyxre'


def func5():
    return (99, 28, 17)


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
