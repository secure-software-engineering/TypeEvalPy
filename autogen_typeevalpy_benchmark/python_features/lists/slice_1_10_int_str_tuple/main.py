# A new list is created as a slice of another one containing functions.


def func1():
    return 74


def func2():
    return 'waafz'


def func3():
    return (91, 21, 25)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
