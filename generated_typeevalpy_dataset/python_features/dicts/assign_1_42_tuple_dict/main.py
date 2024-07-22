# A dictionary key is assigned to a function.


def func1():
    return (46, 96, 70)


def func2():
    return {'vexlc': 37, 'wmfru': 38, 'ihvkf': 55}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
