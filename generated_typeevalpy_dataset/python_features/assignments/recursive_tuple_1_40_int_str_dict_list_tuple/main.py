# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60


def func2():
    return 'hwgtp'


def func3():
    return {'jrvle': 91, 'mzdky': 35, 'hlakh': 36}


def func4():
    return [88, 87, 41]


def func5():
    return (42, 26, 79)


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
