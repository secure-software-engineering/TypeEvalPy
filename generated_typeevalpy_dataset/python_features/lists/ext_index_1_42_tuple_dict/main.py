# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (100, 22, 26)


def func2():
    return {'xngph': 73, 'ejvns': 84, 'kglec': 74}


ls = [func1, func2]

a = ls[key]()
