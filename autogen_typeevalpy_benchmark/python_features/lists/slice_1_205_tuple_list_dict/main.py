# A new list is created as a slice of another one containing functions.


def func1():
    return (84, 66, 91)


def func2():
    return [77, 27, 3]


def func3():
    return {'shrzy': 26, 'wmxee': 89, 'jtlvo': 70}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
