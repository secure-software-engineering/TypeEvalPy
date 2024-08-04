# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [74, 90, 100]


def func2():
    return (20, 29, 29)


def func3():
    return 40


def func4():
    return {'icauo': 2, 'qxvbg': 20, 'qyokg': 15}


def func5():
    return 'ckfdy'


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
