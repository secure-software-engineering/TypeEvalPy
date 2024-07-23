# Nested function calls
# A function `nested_func` return string value
# A function `param_func` is defined which takes a function as a parameter and calls it.
# A function `func` is defined which takes a function 'param_func' as a parameter and calls it with passing another function `nested_func`.


def nested_func():
    return [21, 40, 91]


def param_func(a):
    return a()


def func(a):
    return a(nested_func)


b = param_func
c = func
d = c(b)
