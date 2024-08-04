# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kybko': 72, 'xaohv': 25, 'jcfoo': 86}


def func2():
    return 80.65


def func3():
    return [43, 62, 40]


def func4():
    return (86, 70, 71)


def func5():
    return 'gpmvt'


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
