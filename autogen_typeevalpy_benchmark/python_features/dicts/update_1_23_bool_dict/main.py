# The update method of dictionaries is used.


def func1():
    return {'pucam': 68, 'xrkjk': 68, 'ljklb': 70}


def func2():
    return False


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
