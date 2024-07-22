# A function that returns after computations.


def func():
    return 37.69 + 37.69


a = func()


def func2():
    return 37.69


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + 37.69


c = func5()
