# A key value is imported from an external module and used to access a function stored in a dictionary.


from ext import key


def func():
    return [31, 38, 69]


d = {"a": func}

e = d[key]()
