# A new key-value is added to the dictionary which is a function.


def func():
    return [36, 25, 96]


d = {}

d["b"] = func
e = d["b"]()
