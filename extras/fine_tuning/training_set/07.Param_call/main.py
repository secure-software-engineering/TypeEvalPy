def first_func(func):
    func()


def param_func2():
    return final_func3


def final_func3():
    pass


first_func(param_func2())
