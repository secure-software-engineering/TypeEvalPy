#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'kjtgi':
            return (70, 65, 19)
        case (70, 65, 19):
            return 'kjtgi'
        case _:
            return "default"


a = func('kjtgi')
b = func((70, 65, 19))
c = func([1, 82, 29])
