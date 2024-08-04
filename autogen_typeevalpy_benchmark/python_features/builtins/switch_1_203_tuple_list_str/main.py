#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (15, 34, 89):
            return [18, 12, 48]
        case [18, 12, 48]:
            return (15, 34, 89)
        case _:
            return "default"


a = func((15, 34, 89))
b = func([18, 12, 48])
c = func('kfwze')
