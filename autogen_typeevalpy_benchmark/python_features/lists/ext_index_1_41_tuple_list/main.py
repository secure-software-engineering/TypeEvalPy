# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (4, 84, 18)


def func2():
    return [30, 68, 81]


ls = [func1, func2]

a = ls[key]()
