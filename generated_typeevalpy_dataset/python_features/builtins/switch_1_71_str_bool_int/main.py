#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'nscta':
            return False
        case False:
            return 'nscta'
        case _:
            return "default"


a = func('nscta')
b = func(False)
c = func(63)
