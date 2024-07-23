# A function that returns after computations.


def func():
    return 31 + 31


a = func()


def func2():
    return 31


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + 31


c = func5()
