# A dictionary key is assigned to a function.


def func1():
    return <value1>


def func2():
    return <value2>


d = {"a": func1}

d["a"] = func2

e = d["a"]()
func1()
