# A dictionary key is assigned to a function.


def func1():
    return False


def func2():
    return {'ltpvx': 36, 'zotmv': 65, 'rmqkv': 94}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
