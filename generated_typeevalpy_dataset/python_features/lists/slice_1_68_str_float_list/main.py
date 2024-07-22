# A new list is created as a slice of another one containing functions.


def func1():
    return 'kzrmu'


def func2():
    return 22.48


def func3():
    return [93, 77, 10]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
