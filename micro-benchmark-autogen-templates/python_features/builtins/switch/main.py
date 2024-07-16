#  A function is defined with switch statement in it.
def func(value):
    match value:
        case <value1>:
            return <value2>
        case <value2>:
            return <value1>
        case _:
            return "default"


a = func(<value1>)
b = func(<value2>)
c = func(<value3>)
