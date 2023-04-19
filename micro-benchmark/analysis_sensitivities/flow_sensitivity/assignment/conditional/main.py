# Two variables are assigned a function via chained assignment.


from random import randint


def func1():
    return 42


def func2():
    return "Hello from func2"


if randint(0, 1):
    a = func1
else:
    a = func2


b = a()
