# A new list is created as a slice of another one containing functions.


def func1():
    return [80, 34, 80]


def func2():
    return 'jungw'


def func3():
    return (51, 81, 22)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
