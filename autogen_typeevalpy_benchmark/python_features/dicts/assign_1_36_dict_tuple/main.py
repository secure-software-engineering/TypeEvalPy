# A dictionary key is assigned to a function.


def func1():
    return {'djvwp': 10, 'sawqk': 49, 'fawxq': 20}


def func2():
    return (29, 4, 3)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
