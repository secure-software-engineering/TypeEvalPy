# A new key is added to the dictionary.

def func():
    return "Hello from func"


d = {}

d["b"] = func
e = d["b"]()
