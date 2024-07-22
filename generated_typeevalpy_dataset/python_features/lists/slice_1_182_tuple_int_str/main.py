# A new list is created as a slice of another one containing functions.


def func1():
    return (89, 9, 47)


def func2():
    return 18


def func3():
    return 'qwobu'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
