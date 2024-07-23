# A function that returns after computations.


def func():
    return 64.2 + 64.2


a = func()


def func2():
    return 64.2


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + 64.2


c = func5()
