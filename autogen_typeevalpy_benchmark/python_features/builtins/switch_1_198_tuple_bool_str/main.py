#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (81, 3, 21):
            return False
        case False:
            return (81, 3, 21)
        case _:
            return "default"


a = func((81, 3, 21))
b = func(False)
c = func('avgnr')
