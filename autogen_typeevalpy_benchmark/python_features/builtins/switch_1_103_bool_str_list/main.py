#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 'skrce'
        case 'skrce':
            return False
        case _:
            return "default"


a = func(False)
b = func('skrce')
c = func([49, 30, 65])
