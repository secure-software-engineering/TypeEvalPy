# The update method of dictionaries is used.


def func1():
    return True


def func2():
    return {'scrbr': 84, 'ouzus': 41, 'xcxjy': 61}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
