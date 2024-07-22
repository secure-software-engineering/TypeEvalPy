# A new key-value is added to the dictionary which is a function.


def func():
    return (40, 4, 67)


d = {}

d["b"] = func
e = d["b"]()
