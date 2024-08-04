# A function is called using eval.


def func():
    return (33, 5, 41)


a = eval("func()")
