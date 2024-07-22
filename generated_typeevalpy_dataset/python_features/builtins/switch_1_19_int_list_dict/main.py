#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 63:
            return [56, 50, 21]
        case [56, 50, 21]:
            return 63
        case _:
            return "default"


a = func(63)
b = func([56, 50, 21])
c = func({'gkxkc': 32, 'pqzcs': 96, 'iuusd': 82})
