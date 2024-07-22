# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 65.7


def func2():
    return 63


def func3():
    return {'lgjfq': 92, 'niudw': 91, 'mrawf': 44}


def func4():
    return [36, 10, 97]


def func5():
    return (36, 91, 9)


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
