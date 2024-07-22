# The update method of dictionaries is used.


def func1():
    return {'vnsjp': 41, 'iznqs': 82, 'vnbhz': 49}


def func2():
    return 81.16


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
