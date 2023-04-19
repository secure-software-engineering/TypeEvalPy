# Give as a kwarg a variable previously assigned to a function.


def func2():
    return "Hello from func2"


def func(a):
    return a()


a = func
b = func2
c = a(a=b)
