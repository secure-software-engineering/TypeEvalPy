# Two variables are assigned a function via chained assignment.


def func1():
    return "Hello from func1"


def func2():
    return func1()


a = func2

b = a()


def func2():
    return 42


a = func2

b = a()
