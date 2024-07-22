# A key value is imported from an external module and used to access a function stored in a dictionary.


from ext import key


def func():
    return {'ntdhr': 61, 'ketxa': 76, 'lnjtk': 49}


d = {"a": func}

e = d[key]()
