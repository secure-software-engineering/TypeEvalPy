# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return [48, 55, 47]


def func3():
    return {'uqoqg': 42, 'ishlg': 45, 'zpsik': 72}


def func4():
    return 57.68


def func5():
    return (91, 89, 14)


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
