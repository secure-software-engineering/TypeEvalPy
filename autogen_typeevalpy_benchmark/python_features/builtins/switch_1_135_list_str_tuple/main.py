#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [44, 67, 69]:
            return 'qycun'
        case 'qycun':
            return [44, 67, 69]
        case _:
            return "default"


a = func([44, 67, 69])
b = func('qycun')
c = func((92, 7, 95))
