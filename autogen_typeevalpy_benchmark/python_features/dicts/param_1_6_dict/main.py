# A dictionary is passed as a parameter.


def func2():
    return {'gydud': 41, 'rpkag': 29, 'kvhma': 51}


def func1(d):
    return d["a"]()


d = {"a": func2}

e = func1(d)
