# Two variables are assigned a function via chained assignment.


def func1():
    return 42


def func2():
    return "Hello from func2"


a = func1

b = a()

a = func2

b = a()
