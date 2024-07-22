# A new list is created as a slice of another one containing functions.


def func1():
    return {'ubyoe': 38, 'udhse': 46, 'quygj': 51}


def func2():
    return (56, 64, 16)


def func3():
    return [43, 53, 67]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
