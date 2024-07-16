# A function that returns after computations.


def func():
    return <value1> + <value1>


a = func()


def func2():
    return <value1>


def func3():
    return func2


def func4():
    return func3()


b = func4()()


def func5():
    return func2() + <value1>


c = func5()
