# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (45, 12, 37)


def func2():
    return {'czyas': 85, 'lhuxb': 41, 'rlomt': 49}


ls = [func1, func2]

a = ls[key]()
