# A new key-value is added to the dictionary which is a function.


def func():
    return 'udfcd'


d = {}

d["b"] = func
e = d["b"]()
