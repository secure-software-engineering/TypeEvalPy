# A function that returns after computations.


def func():
    return 71.01 + 71.01


a = func()


def func2():
    return 71.01


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + 71.01


c = func5()
