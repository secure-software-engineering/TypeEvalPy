# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (29, 90, 98)


def func2():
    return 55


def func3():
    return [33, 65, 97]


def func4():
    return 'cnljy'


def func5():
    return {'rzwvh': 53, 'wndjs': 20, 'lmnhs': 26}


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
