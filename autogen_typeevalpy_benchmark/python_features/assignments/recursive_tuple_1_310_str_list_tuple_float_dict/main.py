# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rekfj'


def func2():
    return [36, 32, 92]


def func3():
    return (38, 30, 49)


def func4():
    return 60.44


def func5():
    return {'maygs': 30, 'lukij': 35, 'msxcg': 47}


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
