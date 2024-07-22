# A new list is created as a slice of another one containing functions.


def func1():
    return 'awzxu'


def func2():
    return 59


def func3():
    return (41, 82, 18)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
