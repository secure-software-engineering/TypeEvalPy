# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [28, 18, 42]


def func2():
    return {'rvnie': 83, 'slpfg': 29, 'wjlig': 45}


ls = [func1, func2]

a = ls[key]()
