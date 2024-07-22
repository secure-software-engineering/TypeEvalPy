#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (65, 20, 18):
            return False
        case False:
            return (65, 20, 18)
        case _:
            return "default"


a = func((65, 20, 18))
b = func(False)
c = func('fuevn')
