# Two variables are assigned a function via chained assignment.


def func1():
    return "Hello from func1"


def func2():
    return 42


a = b = func1

c = b()

a = b = func2

d = a()
