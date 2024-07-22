# A function that returns after computations.


def func():
    return 74 + 74


a = func()


def func2():
    return 74


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + 74


c = func5()
