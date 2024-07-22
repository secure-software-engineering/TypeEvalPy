# The update method of dictionaries is used.


def func1():
    return (70, 76, 16)


def func2():
    return {'pgxjr': 60, 'vxwko': 61, 'hywie': 83}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
