# A new key-value is added to the dictionary which is a function.


def func():
    return (17, 93, 83)


d = {}

d["b"] = func
e = d["b"]()
