# A new key-value is added to the dictionary which is a function.


def func():
    return [62, 57, 52]


d = {}

d["b"] = func
e = d["b"]()
