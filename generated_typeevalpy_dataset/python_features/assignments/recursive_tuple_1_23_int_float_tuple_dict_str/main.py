# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 44


def func2():
    return 60.8


def func3():
    return (12, 99, 80)


def func4():
    return {'fbtjq': 30, 'isuyu': 3, 'ifvan': 49}


def func5():
    return 'nhnfv'


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
