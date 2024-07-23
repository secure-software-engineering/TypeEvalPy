# A new list is created as a slice of another one containing functions.


def func1():
    return (93, 59, 35)


def func2():
    return 75


def func3():
    return {'ikuan': 47, 'rwkhr': 92, 'uufgf': 55}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
