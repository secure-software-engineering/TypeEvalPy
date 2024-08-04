# The update method of dictionaries is used.


def func1():
    return False


def func2():
    return {'sodfw': 89, 'heqzh': 6, 'madxd': 51}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
