# A new list is created as a slice of another one containing functions.


def func1():
    return 42


def func2():
    return 42.5


def func3():
    return "Hello from func3"


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
func1(); func3()
