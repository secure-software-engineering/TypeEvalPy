# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88.61


def func2():
    return 98


def func3():
    return (25, 72, 47)


def func4():
    return 'hivpe'


def func5():
    return {'jxcuh': 4, 'ctrqo': 50, 'ljmuf': 9}


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
